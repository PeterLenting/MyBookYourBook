from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import RentRequestForm
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product


@login_required()
def rent_view(request):
    user = User.objects.get(username=request.user.username)
    cart = request.session.get('cart', {})
    total = 0
    product_ids = []
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.rentprice_per_week
        product_ids.append(id)
    data = {'username': request.user,
            'email': user.email,
            'total_amount': total,
            'books': product_ids}
    form = RentRequestForm(initial=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            messages.error(request,
                           "We were unable to recieve your order")
    else:
        form = RentRequestForm()

    return render(request, "rent.html",
                  {"form": form})
