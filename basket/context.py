from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """
    Shows the contents within basket.
    Displays quantities and checks for sizes.

    Placed in settings.py, made available to all templates.
    Display delivery threshold.

    FREE_DELIVERY_THRESHOLD = 100
    STANDARD_DELIVERY_PERCENTAGE = 10
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        # Check if item has no size.
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data 
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else: 
            # Else there is a size, data is kept as a dictionary, iterate through dictionary.
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['item_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'basket': basket,
    }

    return context