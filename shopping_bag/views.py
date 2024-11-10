from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the shopping bag page """
    return render(request, 'shopping_bag/bag.html')


def add_to_bag(request, item_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity', 1))
        redirect_url = request.POST.get('redirect_url', '/products/')
        
        bag = request.session.get('bag', {})       
       
        if str(item_id) in bag:
            bag[str(item_id)] += quantity
        else:
            bag[str(item_id)] = quantity
        
        request.session['bag'] = bag
        messages.success(request, f'Added {product.name} to your bag.')

        return HttpResponseRedirect(redirect_url)
    return redirect('products')


# Update quatity of products
def update_bag(request, item_id):
    """Update the quantity of the specified item in the shopping bag."""
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    item_id = str(item_id)

    action = request.POST.get('action')
    if action == 'increase':
        bag[item_id] = bag.get(item_id, 0) + 1
        messages.success(request, f'Increased {product.name} quantity.')
    elif action == 'decrease':
        if item_id in bag:
            if bag[item_id] > 1:
                bag[item_id] -= 1
                messages.success(request, f'Decreased {product.name} quantity.')
            else:
                del bag[item_id]
                messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect('view_bag')


# Remove a single item from bag
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag."""
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    item_id = str(item_id)

    if item_id in bag:
        del bag[item_id]
        messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect('view_bag')


# Clear Bag View
def clear_bag(request):
    """ Clear all items from the shopping bag """
    if 'bag' in request.session:
        del request.session['bag']
        messages.success(request, "Shopping bag cleared successfully.")
    return redirect('view_bag')