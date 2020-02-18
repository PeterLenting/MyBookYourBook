from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    cart_ids = []
    total = 0
    quantity = 1

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        cart_ids.append(int(id))

    return {'cart_items': cart_items, 'total': total, "cart_ids": cart_ids}
