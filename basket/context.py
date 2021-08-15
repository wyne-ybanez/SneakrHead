from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404


def basket_contents(request):
    """
    Placed in settings.py, made available to all templates.
    Display delivery threshold.
    FREE_DELIVERY_THRESHOLD = 100
    STANDARD_DELIVERY_PERCENTAGE = 10
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

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
    }

    return context