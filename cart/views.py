from django.shortcuts import render, redirect, reverse


# Renders cart contents page
def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "cart.html")


# Adds the specified book to the cart when the user is logged in.
# If user is not logged in, he is send to login page.
def add_to_cart(request, id):
    quantity = 1
    cart = request.session.get('cart', {})
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        cart[id] = cart.get(id, quantity)
        request.session['cart'] = cart
    return redirect(reverse('get_products'))


# Removes specified book from the cart
def remove_item(request):
    id = request.POST['product_id']
    cart = request.session.get('cart', {})
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')
