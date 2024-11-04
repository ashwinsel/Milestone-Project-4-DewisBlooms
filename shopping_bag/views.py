from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product

def shopping_cart(request):
    """
    Display the shopping cart with all items, quantities, and total amount.
    """
    # Get the cart data from the session (initialize as empty dict if not present)
    cart = request.session.get('cart', {})

    # Initialize cart items list and total cost
    cart_items = []
    total = 0

    # Loop over each item in the cart to gather necessary information
    for product_id, item in cart.items():
        try:
            # Fetch the product from the database using the product_id
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            # Skip this item if the product does not exist in the database
            print(f"Product with id {product_id} does not exist.")
            continue

        # Extract quantity and calculate item total
        quantity = item['quantity']
        item_total = product.price * quantity
        total += item_total  # Update total cost

        # Append item details to cart_items list
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'image': product.image.url,  # Assuming Product model has an image field
            'price': product.price,
            'quantity': quantity,
            'subtotal': item_total,
        })

    # Debugging output
    print("Cart Items:", cart_items)
    print("Total Cart Value:", total)

    # Prepare context for rendering the shopping cart template
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shopping_bag/shopping_cart.html', context)

def remove_from_cart(request, product_id):
    """
    Remove an item from the cart using its product_id.
    """
    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Remove the item if it exists in the cart
    if str(product_id) in cart:  # Ensure product_id is a string to match session data keys
        del cart[str(product_id)]
        request.session['cart'] = cart  # Update session data
        messages.success(request, "Item removed from cart.")
        print(f"Removed product with id {product_id} from cart.")
    else:
        print(f"Product with id {product_id} was not found in the cart.")

    # Redirect to the shopping cart page
    return redirect(reverse('shopping_bag:shopping_cart'))

def clear_cart(request):
    """
    Clear all items from the cart.
    """
    # Clear the cart in session
    request.session['cart'] = {}
    messages.success(request, "Cart cleared.")
    print("Cart has been cleared.")
    return redirect(reverse('shopping_bag:shopping_cart'))

def add_to_cart(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag.
    """
    # Fetch the product from the database
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if no quantity is provided
    
    # Get the cart from the session or initialize a new one
    cart = request.session.get('cart', {})
    
    # Update the cart with the specified quantity
    item_id_str = str(item_id)  # Ensure the key is a string for consistency
    if item_id_str in cart:
        cart[item_id_str]['quantity'] += quantity
    else:
        cart[item_id_str] = {'quantity': quantity, 'price': str(product.price)}
    
    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Debugging output
    print(f"Added {quantity} of product id {item_id} to the cart.")
    print("Updated Cart:", cart)

    # Calculate and update the total amount for the cart
    cart_total = sum(
        int(item['quantity']) * float(item['price'])
        for item in cart.values()
    )
    request.session['cart_total'] = round(cart_total, 2)  # Store total in session

    # Redirect back to the product detail page (replace 'product_detail' with the correct view name if necessary)
    return redirect('products:product_detail', item_id=item_id)