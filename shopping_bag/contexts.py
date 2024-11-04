from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})
    free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    delivery = Decimal(0)

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price  # Calculate subtotal here
        total += subtotal  # Add subtotal to total
        product_count += quantity
        
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,  # Add subtotal to each item
        })

    # Add delivery costs logic
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * (settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context