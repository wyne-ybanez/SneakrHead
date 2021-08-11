from django.shortcuts import render
from products.models import Product


def index(request):
    """ 
    View to return the index page.
    Display Products
    """
    products = Product.objects.all()
    featured_products = Product.objects.filter(featured_product=True)
    new_products = Product.objects.filter(new_product=True)

    context = {
        'products': products,
        'featured_products': featured_products,
        'new_arrivals': new_products,
    }

    return render(request, 'home/index.html', context)