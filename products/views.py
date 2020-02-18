from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseForbidden
from django.contrib import messages


def get_rent_products(request):
    """
    Create a view that will return a list
    of all Products that were published prior to 'now'
    and render them to the 'products.html' template
    """
    products = Product.objects.filter(is_for_rent=True,
                                      published_date__lte=timezone.now(
                                      )).order_by('-published_date')
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


def get_sale_products(request):
    """
    Create a view that will return a list
    of all Products that were published prior to 'now'
    and render them to the 'products.html' template
    """
    products = Product.objects.filter(is_for_sale=True,
                                      published_date__lte=timezone.now(
                                      )).order_by('-published_date')
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


def get_products(request):
    """
    Create a view that will return a list
    of all Products that are for rent and that were published prior to 'now'
    and render them to the 'products.html' template
    """
    products = Product.objects.filter(
               published_date__lte=timezone.now()).order_by('-published_date')
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


def product_detail(request, pk):
    """
    Create a view that returns a single
    Product object based on the product ID (pk) and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    return render(request, "productdetail.html", {'product': product})


def edit_product(request, pk=None):
    """
    Create a view that allows user to edit
    his own product and a superuser to edit all products.
    """
    products = get_object_or_404(Product, pk=pk)
    if (request.user == products.provider or
            request.user.is_superuser):
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=products)
            if form.is_valid():
                products = form.save()
                return redirect(product_detail, products.pk)
        else:
            form = ProductForm(instance=products)
    else:
        return HttpResponseForbidden()

    return render(request, 'productform.html', {'form': form})


def new_product(request, pk=None):
    """
    Create a view that allows user to add
    a new book.
    """
    product = get_object_or_404(Product, pk=pk) if pk else None
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.provider = request.user
                product.save()
                return redirect('get_products')
        else:
            form = ProductForm()
    return render(request, 'productform.html', {'form': form})


def delete_product(request, pk=None):
    """
    Create a view that allows user to delete
    his own product and a superuser to delete all products.
    """
    product_id = int(pk)
    product = get_object_or_404(Product, pk=product_id)
    if (request.user == product.provider or
            request.user.is_superuser):
        if request.method == 'POST':
            try:
                product.delete()
                messages.success(request,
                                 'You have successfully deleted your product')
            except Product.DoesNotExist:
                messages.warning(request, 'The product could not be deleted')
    else:
        return HttpResponseForbidden(
               'You are only allowed to delete your own products')

    return redirect('get_products')
