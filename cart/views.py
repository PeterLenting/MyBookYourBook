from django.shortcuts import render, redirect, reverse


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
