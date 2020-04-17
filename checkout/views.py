from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.contrib.auth.models import User
from accounts.models import UserProfile
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
                customer = stripe.Charge.create(
                    amount=3000,
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
                print("D")
                order.have_paid = True
                print(order.have_paid)
                print(request.session['user_email'])
                user = User.objects.get(email=request.session['user_email'])
                order.user = user
                order.save()
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                print("PAID")
                user_profile = UserProfile.objects.filter(user=order.user).first()
                user_profile.have_paid = True
                user_profile.save()
                messages.error(request,
                               "You have successfully paid, start shopping :)")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
                print("Unable to take payment")
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
