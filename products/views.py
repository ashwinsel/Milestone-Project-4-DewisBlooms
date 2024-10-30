from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

def all_products(request):
    """A view to show all products, including sorting and search queries."""
    products = Product.objects.all()
    query = request.GET.get('q', None)
    category_name = request.GET.get('category', None)
    categories = Category.objects.all()
    current_categories = []

    # Category filtering
    if category_name:
        category_list = category_name.split(',')
        products = products.filter(category__name__in=category_list)
        current_categories = Category.objects.filter(name__in=category_list)

    # Search query filtering
    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'current_categories': current_categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display individual product details."""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_to_cart(request, product_id):
    """Add a product to the shopping cart."""
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart_total = request.session.get('cart_total', 0)

    # Increment quantity if product already in cart, else add new entry
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    # Update total price
    cart_total += float(product.price)
    request.session['cart'] = cart
    request.session['cart_total'] = cart_total

    messages.success(request, f'Added {product.name} to your cart.')
    return redirect(reverse('products'))


def shopping_cart(request):
    """A view to display the shopping cart contents."""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total_price = product.price * item_data['quantity']
        total += total_price
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'total_price': total_price
        })

    context = {
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'shopping_bag/shopping_cart.html', context)