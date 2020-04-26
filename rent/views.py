from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RentRequestForm
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Product


# How the user rents a book:
# After adding books to his cart, the logged in user goes to his Cart page.
# On the Cart page logged in user can see the books that are is his cart,
# and has the possibility to remove books from his cart.
# If all is good, the Let's rent button takes him to the (hidden) rent form.
# After sending in the form, Admin can see which user wants what books.
# Users is send to rent_succes page.

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
            messages.success(request,
                             "Great, we recieved your order!\
                             <br/>We will contact the owners of the books \
                             you want to rent and have them contact you.\
                             <br/>Have a great day!")
            return redirect('get_products')
        else:
            messages.error(request,
                           "We were unable to recieve your order")
    else:
        form = RentRequestForm(initial=data)

    return render(request, "rent.html", {"form": form})
