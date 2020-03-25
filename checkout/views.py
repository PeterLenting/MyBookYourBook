from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
# from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
# from products.models import Product
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        print("A")
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        print("B")
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            print("C")
            try:
                print("D")
                customer = stripe.Charge.create(
                    amount=3000,
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
                order.have_paid = True
                print(order.have_paid)
                print("E")
                order.save()
                messages.error(request,
                               "You have successfully paid, start shopping :)")
                return redirect(reverse('profile'))
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
        else:
            print(payment_form.errors)
            messages.error(request,
                           "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {
                  'order_form': order_form,
                  'payment_form': payment_form,
                  'publishable': settings.STRIPE_PUBLISHABLE})
