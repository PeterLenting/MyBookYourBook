from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.conf import settings
from django.utils import timezone
import stripe


stripe.api_key = settings.STRIPE_SECRET


# How the user pays his deposit:
# After checking the want_to_rent checkbox in the UserProfileForm
# user is taken to the checkout page.
# There the logged in User fills and sends in OrderForm and MakePaymentForm.
# If both are valid 30 euro is paid have_paid is set to True,
# so Admin can see the user has paid.
# When all is successfull user is send to his Profile page.
@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            try:
                customer = stripe.Charge.create(
                    amount=3000,
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
                order.have_paid = True
                user = User.objects.get(email=request.session['user_email'])
                order.user = user
                order.save()
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                user_profile = UserProfile.objects.filter(
                               user=order.user).first()
                user_profile.have_paid = True
                user_profile.save()
                messages.info(request,
                              "You have successfully paid, start shopping :)")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request,
                           "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", {
                  'order_form': order_form,
                  'payment_form': payment_form,
                  'publishable': settings.STRIPE_PUBLISHABLE})
