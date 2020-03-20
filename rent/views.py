from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RentRequestForm
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product


def rent_success_view(request):
    """Return the rent_success.html file"""
    return render(request,  'rent_success.html')


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
        y = ','.join(product_ids)  # converting list into string
    data = {'username': request.user.username,
            'email': user.email,
            'total_amount': int(total),
            'books': y}
    if request.method == "POST":
        form = RentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['cart'] = {}
            return redirect('rent_succes')
        else:
            print(form.errors)
            messages.error(request,
                           "We were unable to recieve your order")
    else:
        form = RentRequestForm(initial=data)

    return render(request, "rent.html", {"form": form})
