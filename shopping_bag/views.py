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
        quantity = int(request.POST.get('quantity', 1))
        redirect_url = request.POST.get('redirect_url', '/products/')
        
        bag = request.session.get('bag', {})
        
        print("Initial bag contents:", bag)  # Debug: print initial bag

        if str(item_id) in bag:
            bag[str(item_id)] += quantity
        else:
            bag[str(item_id)] = quantity
        
        request.session['bag'] = bag

        return HttpResponseRedirect(redirect_url)
    return redirect('products')


# Clear Bag View
def clear_bag(request):
    """ Clear all items from the shopping bag """
    if 'bag' in request.session:
        del request.session['bag']
        messages.success(request, "Shopping bag cleared successfully.")
    return redirect('view_bag')