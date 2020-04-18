from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product
from accounts.forms import (
                            UserLoginForm,
                            UserRegistrationForm,
                            UserProfileForm,
                            EditUserForm,
                            EditUserProfileForm,
                            )


def registration(request):
    """Render the registration page"""
    checked_box_value = request.POST.get('want_to_rent')
    if request.user.is_authenticated:
        return redirect(reverse('get_products'))
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print(registration_form.errors)
        if registration_form.is_valid() and profile_form.is_valid():
            print(registration_form.errors)
            print(profile_form.errors)
            print("TEST A")
            user = registration_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print("TEST B")
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if (checked_box_value == 'on' and user):
                auth.login(user=user, request=request)
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                print("TEST C")
                return redirect('checkout')
            elif user:
                auth.login(user=user, request=request)
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                print("TEST D")
                return redirect(reverse('get_products'))
            else:
                messages.error(request,
                               "Sorry, we are unable to register your account at this time")
                return redirect(reverse('registration'))
        else:
            print("TEST E")
            print(registration_form.errors)
            print(profile_form.errors)
            return redirect(reverse('registration'))
    else:
        print("TEST A1")
        registration_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {
            "registration_form": registration_form,
            "profile_form": profile_form})


# If a user is not logged in, the login view lets him log in.
# After fillingin and sendin in a valid login form, the user is logged in.
# The logged in user is send to the homepage.

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('get_products'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                return redirect(reverse('get_products'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


# To let the logged in user log out:
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('get_products'))


# Let's the logged in user take a look at his own profile.
# Shows some personal data and all the books he has on offer.

def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    user_posts = Product.objects.filter(provider=request.user).order_by(
                 '-published_date')
    return render(request,
                  'profile.html', {"user": user, 'user_posts': user_posts})


# Let's the logged in user update his own profile.
# If EditUserForm and EditUserProfileForm are valid the profile is updated,
# and the user is send to his updated profile.

@login_required
def update_profile(request):
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        edit_user_form = EditUserForm(
            request.POST,
            instance=request.user
        )
        user_profile_form = EditUserProfileForm(
            request.POST,
            instance=request.user.uprofile
        )
        if edit_user_form.is_valid() and user_profile_form.is_valid():
            edit_user_form.save()
            user_profile_form.save()
            return redirect(reverse("profile"))
    else:
        edit_user_form = EditUserForm(
            instance=request.user
        )
        user_profile_form = EditUserProfileForm(
            instance=request.user.uprofile
        )
    args = {'form': edit_user_form,
            'formUserProfile': user_profile_form,
            'user': user}
    return render(request, 'update_profile.html', args)


# Let's logged in user look at other users profile
# Logged in user can click on the name of the provider of each book.
# In the profile some data and all the books the provider offers are shown.

def provider_profile(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        provider = get_object_or_404(User, pk=pk)
        user_posts = Product.objects.filter(provider_id=provider.id).order_by(
                        '-published_date')
        return render(request, 'profile.html', {"user": provider,
                      'user_posts': user_posts})
