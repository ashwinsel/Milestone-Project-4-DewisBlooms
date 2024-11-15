from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shopping_bag.contexts import bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data for a Stripe payment intent.

    This view modifies the Stripe payment intent to include metadata about the 
    user's shopping bag, save information preference, and username.

    Args:
        request (HttpRequest): The HTTP request object containing POST data.

    Returns:
        HttpResponse: A status 200 response if successful, otherwise a 400 response 
        with the error content.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': str(request.user),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handle the checkout process.

    This view handles both GET and POST requests for the checkout page. It validates
    form data, processes orders, and integrates with Stripe for payment.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the checkout page or redirects to another view based on
        the request method and form validation.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag')
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment.")
            return redirect(reverse('products'))

        form_data = {key: request.POST[key] for key in [
            'full_name', 'email', 'phone_number', 'country', 
            'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county']}
        
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_pid = request.POST.get('client_secret', '').split('_secret')[0]
            order.original_bag = json.dumps(bag)
            order.save()

            # Process order items
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    quantity = item_data if isinstance(item_data, int) else item_data.get('quantity', 0)
                    OrderLineItem.objects.create(order=order, product=product, quantity=quantity)
                except Product.DoesNotExist:
                    messages.error(request, "A product in your bag wasn't found.")
                    order.delete()
                    return redirect(reverse('view_bag'))
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double-check your information.')

    else:
        bag = request.session.get('bag')
        if not bag:
            messages.error(request, "Your bag is empty!")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=round(current_bag['grand_total'] * 100),
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    return render(request, template, {'order_form': order_form, 'stripe_public_key': stripe_public_key, 'client_secret': intent.client_secret})


def checkout_success(request, order_number):
    """
    Handle successful checkouts.

    This view finalizes the checkout process by saving user profile information, 
    clearing the shopping bag, and providing a success message to the user.

    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): The unique order number.

    Returns:
        HttpResponse: Renders the checkout success page.
    """
    order = get_object_or_404(Order, order_number=order_number)
    if 'bag' in request.session:
        del request.session['bag']

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    messages.success(request, f'Order processed! Your order number is {order_number}. Confirmation sent to {order.email}.')
    return render(request, 'checkout/checkout_success.html', {'order': order})