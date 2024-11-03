from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

def shopping_cart(request):
    """ A view to show the shopping cart page """
    # Retrieve the cart items from the session
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            total += product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity
            })
        except Product.DoesNotExist:
            messages.error(request, "A product in your cart does not exist.")

    context = {
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'shopping_bag/shopping_cart.html', context)

def remove_from_cart(request, product_id):
    """ A view to remove a product from the shopping cart """
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, "Removed item from cart")

    return redirect('shopping_cart')

def clear_cart(request):
    """ A view to clear all items in the shopping cart """
    request.session['cart'] = {}
    messages.success(request, "Cleared all items in cart")
    return redirect('shopping_cart')