from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    category_name = request.GET.get('category')
    categories = Category.objects.all()
    current_categories = []

    # Check for category filtering
    if category_name:
        # Split by comma in case multiple categories are requested
        category_list = category_name.split(',')
        # Filter products by categories
        products = products.filter(category__name__in=category_list)
        current_categories = Category.objects.filter(name__in=category_list)

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
        'categories': categories,  # All categories for filtering options
        'current_categories': current_categories,  # Selected categories
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """View to display a single product's detail"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)