from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the shopping bag page """
    return render(request, 'shopping_bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Retrieve product and quantity
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Retrieve or create the bag in session
    bag = request.session.get('bag', {})

    # Add or update the quantity in bag
    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Save updated bag in session
    request.session['bag'] = bag
    messages.success(request, f'Added {product.name} to your bag')

    return redirect(redirect_url)