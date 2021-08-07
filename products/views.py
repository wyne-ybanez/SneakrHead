from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ 
    A view to show individual product details 
    """

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()

    url = 'products/product_detail.html'
    context = {
        'product': product,
        'products': products,
    }

    return render(request, url, context)