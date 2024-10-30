from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def product_detail(request, product_id):
    """View to display a single product's detail"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def all_products(request):
    products = Product.objects.all()
    query = None

    # Check if there is a search query
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        # Use Q objects to allow searching in either name or description
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)