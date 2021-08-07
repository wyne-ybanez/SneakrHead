from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ A View to show all products.
    Includes sorting and search queries.
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET: 
            query = request.GET['q']
            if not query: 
                messages.error(request, "Oops! You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    url = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
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