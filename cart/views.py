from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add the specified product to the cart when the user is logged in"""
    quantity = 1
    cart = request.session.get('cart', {})
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if id in cart:
            cart[id] = int(cart[id]) + quantity
        else:
            cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
    return redirect(reverse('get_products'))


def remove_item(request):
    """Removes item from the cart"""
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')
