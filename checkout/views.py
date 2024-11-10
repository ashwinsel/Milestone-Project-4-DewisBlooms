from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty! Please add items before proceeding to checkout.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        
    }
    return render(request, 'checkout/checkout.html', context)