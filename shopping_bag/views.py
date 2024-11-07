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
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if no quantity provided
        redirect_url = request.POST.get('redirect_url', '/')
        bag = request.session.get('bag', {})
        bag[item_id] = bag.get(item_id, 0) + quantity
        request.session['bag'] = bag
        return HttpResponseRedirect(redirect_url)
    return redirect('products')