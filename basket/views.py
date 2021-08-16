from django.shortcuts import render, redirect


def view_basket(request):
    """
    A view to return the shopping basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a quanitity of the desired product and place it in basket.
    Stores shopping basket data in a 'session'.
    Get 'basket' in session or create basket object if it doesn't exist.
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    return redirect(redirect_url)