from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

from decimal import Decimal


def all_products(request):
    """ A View to show all products.
    Includes sorting and search queries.
    """
    products = Product.objects.all()
    featured_products = Product.objects.filter(featured_product=True)
    query = None
    price_range = None
    categories = None
    sort = None
    direction = None
    stock = None

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

        if 'in_stock' in request.GET: 
            products = products.filter(stock=True)
            stock = True

        if 'no_stock' in request.GET: 
            products = products.filter(stock=False)
            stock = False

        if 'price_range' in request.GET:
            price_range = request.GET['price_range']
            products = products.filter(price__lte=Decimal(price_range))

    current_sorting = f'{sort}_{direction}'

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'price_range': price_range,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'featured_products': featured_products,
        'stock': stock,
    }
    return render(request, template, context)


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


@login_required
def add_product(request):
    """ 
    Add a product to the store.
    Displays number of products. 
    """
    products = Product.objects.all()
    in_stock = Product.objects.filter(stock=True)
    out_of_stock = Product.objects.filter(stock=False)
    featured = Product.objects.filter(featured_product=True)
    new_arrivals = Product.objects.filter(new_product=True)
    brand_item = Product.objects.filter(brand_item=True)
    five_star_product = Product.objects.filter(rating__gte=5)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners and trusted partners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'products': products,
        'products_in_stock': in_stock,
        'products_out_of_stock': out_of_stock,
        'featured': featured,
        'new_arrivals': new_arrivals,
        'brand_item': brand_item,
        'five_star_product': five_star_product,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Edit a product in the store 
    """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners and trusted partners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ 
    Delete a product from the store 
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners and trusted partners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))