from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product
from accounts.forms import (
                            UserLoginForm,
                            UserRegistrationForm,
                            UserProfileForm,
                            EditProfileForm,
                            EditUserProfileForm,
                            )
"""from accounts.models import UserProfile"""


def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('get_products'))


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
                return redirect(reverse('get_products'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('get_products'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if registration_form.is_valid():
            print("Got this part working")
        if profile_form.is_valid():
            print("Got the profile part working")
        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request,
                               "Sorry, we are unable to register your account at this time")
        else:
            print("SOMETHING WENT WRONG")
    else:
        registration_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form, 'profile_form': profile_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    user_posts = Product.objects.filter(provider=request.user).order_by('-published_date')
    return render(request, 'profile.html', {"user": user, 'user_posts': user_posts})


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        formUserProfile = EditUserProfileForm(request.POST,
                                              instance=request.user.uprofile)

        if form.is_valid() and formUserProfile.is_valid():
            user = formUserProfile.save()
            profile = form.save(commit=False)
            request.user = user
            profile.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        formUserProfile = EditUserProfileForm(instance=request.user.uprofile)
        args = {'form': form, 'formUserProfile': formUserProfile}
        return render(request, 'update_profile.html', args)
