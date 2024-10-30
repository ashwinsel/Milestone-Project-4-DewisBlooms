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


def add_to_cart(request, product_id):
    """Add a product to the shopping cart and update the total."""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart_total = request.session.get('cart_total', 0)

    # Add the product to the cart
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    # Update the total in the session
    cart_total += float(product.price)
    request.session['cart'] = cart
    request.session['cart_total'] = cart_total

    messages.success(request, f'Added {product.name} to your cart.')
    return redirect(reverse('products'))