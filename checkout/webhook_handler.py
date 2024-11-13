from django.http import HttpResponse
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
import stripe
import json
import time

class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unexpected webhook event"""
        return HttpResponse(content=f'Unhandled event: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle successful payments"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(content=f'Successful payment for existing order: {event["type"]}', status=200)
        else:
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(order=order, product=product, quantity=item_data)
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook error: {e}', status=500)

        return HttpResponse(content=f'Order created on successful payment: {event["type"]}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle failed payments"""
        return HttpResponse(content=f'Failed payment: {event["type"]}', status=200)