from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def all_products(request):
    """ A View to show all products.
    Includes sorting and search queries.
    """
    products = Product.objects.all()
    featured_products = Product.objects.filter(featured_product=True)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                # Annotate into field
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
    
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET: 
            query = request.GET['q']
            if not query: 
                messages.error(request, "Oops! You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    url = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'featured_products': featured_products
    }
    return render(request, url, context)


def product_detail(request, product_id):
    """ 
    A view to show individual product details 
    """
    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    featured_products = Product.objects.filter(featured_product=True)

    url = 'products/product_detail.html'
    context = {
        'product': product,
        'products': products,
        'featured_products': featured_products,
    }

    return render(request, url, context)