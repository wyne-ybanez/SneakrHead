from django.shortcuts import render
from products.models import Product


def index(request):
    """ 
    View to return the index page.
    Display Products
    """

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'home/index.html', context)