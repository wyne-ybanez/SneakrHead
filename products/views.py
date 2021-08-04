from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A View to show all products.
    Includes sorting and search queries.
    """

    products = Product.objects.all()

    url = 'products/products.html'
    context = {
        'products': products
    }
    return render(request, url, context)