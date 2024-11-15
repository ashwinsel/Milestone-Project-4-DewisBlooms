from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product, Category
from django.contrib.auth.decorators import login_required


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    Supports category filtering, text search, and sorting by fields.
    """
    products = Product.objects.all()
    query = request.GET.get('q')
    category_name = request.GET.get('category')
    sort = request.GET.get('sort')
    direction = request.GET.get('direction', 'asc')

    # Filter by category
    if category_name:
        category_list = category_name.split(',')
        products = products.filter(category__name__in=category_list)

    # Filter by search query
    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    # Sorting
    if sort:
        if sort == 'name':
            products = products.annotate(lower_name=Lower('name'))
            sort = 'lower_name'
        sortkey = f'-{sort}' if direction == 'desc' else sort
        products = products.order_by(sortkey)

    context = {
        'products': products,
        'search_term': query,
        'categories': Category.objects.all(),
        'current_sorting': f'{sort}_{direction}',
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to display individual product details.
    Allows logged-in users to add a rating for the product.
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST' and request.user.is_authenticated:
        try:
            rating = float(request.POST.get('rating'))
            if 0 <= rating <= 5:
                product.rating = rating
                product.save()
                messages.success(request, f'Your rating of {rating} has been added!')
            else:
                messages.error(request, 'Rating must be between 0 and 5.')
        except ValueError:
            messages.error(request, 'Invalid rating value.')

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_to_cart(request, product_id):
    """
    Add a product to the shopping cart.
    Updates the session cart and the total price in the session.
    """
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart_total = request.session.get('cart_total', 0)

    # Increment or add product
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }

    # Update total price
    request.session['cart'] = cart
    request.session['cart_total'] = cart_total + float(product.price)
    messages.success(request, f'Added {product.name} to your cart.')

    return redirect(reverse('products'))


def shopping_cart(request):
    """
    A view to display the shopping cart contents.
    Combines session data with product information for display.
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(pk__in=product_ids)

    for product in products:
        item_data = cart.get(str(product.id))
        quantity = item_data['quantity']
        total_price = product.price * quantity
        total += total_price
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'shopping_bag/shopping_cart.html', context)