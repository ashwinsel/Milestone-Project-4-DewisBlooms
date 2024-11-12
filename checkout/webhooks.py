import stripe
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Order

@csrf_exempt
def stripe_webhook(request):
    # Get webhook data from Stripe
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event type
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_number = payment_intent['metadata']['order_number']
        try:
            order = Order.objects.get(order_number=order_number)
            order.payment_status = 'Paid'  # Customize if you have a status field
            order.save()
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        
    # Add handling for other events if needed

    return HttpResponse(status=200)