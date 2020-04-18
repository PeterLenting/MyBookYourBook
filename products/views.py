from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Product
from .forms import UserContactForm
from .forms import ProductForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


# Lets the logged in user send and email to another user
# On clicking the Buy button for a book the user is taken
# to the usercontactpage. There a default email is set up
# using the het email and first name of the request.user and of
# the provider of the book and the title of the book.
# The message is send to the provider of the book.
def user_contact_form_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        product = get_object_or_404(Product, pk=pk)
        user = User.objects.get(username=request.user.username)
        if request.method == 'GET':
            data = {'subject': "I would like to buy " + product.title,
                    'message': "Dear " + product.provider.first_name +
                    ", \n\nI would like to buy your copy of " + product.title +
                    ". \nYou can contact me at " + user.email +
                    ".\n\nKind regards, " + user.first_name}
            form = UserContactForm(initial=data)
        else:
            form = UserContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = user.email
                message = form.cleaned_data['message']
                to_email = [product.provider.email]
                try:
                    send_mail(subject,
                              message,
                              from_email,
                              to_email)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request,
                                 "Your message has been send, \
                                 you can continue shopping")
                return redirect(reverse('get_products'))
        return render(request, "usercontactpage.html",
                      {'form': form, 'product': product})


# Create a view that will return a list
# of all Products that were published prior to 'now'
# and render them to the 'products.html' template
def get_my_products(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        products = Product.objects.filter(provider=request.user,
                                          published_date__lte=timezone.now(
                                          )).order_by('-published_date')
        for p in products:
            print(p)
        return render(request, "products.html", {'products': products})


# Create a view that will return a list
# of all Products that were published prior to 'now'
# and render them to the 'products.html' template
def get_rent_products(request):
    products = Product.objects.filter(is_for_rent=True,
                                      published_date__lte=timezone.now(
                                      )).order_by('-published_date')
    if request.user.is_authenticated():
        products = Product.objects.filter(
                   is_for_rent=True,
                   published_date__lte=timezone.now(
                   )).order_by('-published_date').exclude(
                   provider=request.user)
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


# Create a view that will return a list
# of all Products that were published prior to 'now'
# and render them to the 'products.html' template
def get_sale_products(request):
    products = Product.objects.filter(is_for_sale=True,
                                      published_date__lte=timezone.now(
                                      )).order_by('-published_date')
    if request.user.is_authenticated():
        products = Product.objects.filter(
                   is_for_sale=True,
                   published_date__lte=timezone.now(
                   )).order_by('-published_date').exclude(
                   provider=request.user)
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


# Create a view that will return a listof all Products
# that are for rent, that were published prior to 'now',
# that are not published by the logged in user
# and render them to the 'products.html' template
def get_products(request):
    products = Product.objects.filter(published_date__lte=timezone.now(
                                      )).order_by('-published_date')
    if request.user.is_authenticated():
        products = Product.objects.filter(
                   published_date__lte=timezone.now(
                   )).order_by('-published_date').exclude(
                   provider=request.user)
    for p in products:
        print(p)
    return render(request, "products.html", {'products': products})


# Create a view that returns a single Product object
# based on the product ID (pk) and render to 'productdetail.html' template.
# Return a 404 error if the product is not found
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    return render(request, "productdetail.html", {'product': product})


# Create a view that allows user to edit his own product
# and a superuser to edit all products.
def edit_product(request, pk=None):
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


# Create a view that allows user to add
# a new book.
def new_product(request, pk=None):
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
                return redirect('get_my_products')
        else:
            form = ProductForm()
    return render(request, 'productform.html', {'form': form})


# Create a view that allows user to delete his own product
# and a superuser to delete all products.
def delete_product(request, pk=None):
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
