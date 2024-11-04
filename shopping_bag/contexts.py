from decimal import Decimal
from django.conf import settings
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    delivery = Decimal(0)

    for item_id, quantity in bag.items():
        product = Product.objects.get(id=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product': product,
            'quantity': quantity,
        })

    # Add delivery costs logic
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * (settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context