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
                            )


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
    checked_box_value = request.POST.get('want_to_rent')
    if request.user.is_authenticated:
        return redirect(reverse('get_products'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if (checked_box_value == 'on' and user):
                auth.login(user=user, request=request)
                return redirect('checkout')
            elif user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('get_products'))
            else:
                messages.error(request,
                               "Sorry, we are unable to register your account at this time")
                return redirect(reverse('registration'))
        else:
            return redirect(reverse('registration'))
    else:
        registration_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {
            "registration_form": registration_form,
            "profile_form": profile_form})


def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    user_posts = Product.objects.filter(provider=request.user).order_by(
                 '-published_date')
    return render(request,
                  'profile.html', {"user": user, 'user_posts': user_posts})


@login_required
def update_profile(request):
    user = User.objects.get(email=request.user.email)
    # form = EditUserForm(request.POST)
    # formUserProfile = EditUserProfileForm(request.POST)
    if request.method == 'POST':
        edit_user_form = EditUserForm(
            request.POST,
            instance=request.user
        )
        user_profile_form = UserProfileForm(
            request.POST,
            instance=request.user.uprofile
        )
        if edit_user_form.is_valid() and user_profile_form.is_valid():
            edit_user_form.save()
            user_profile_form.save()
            messages.success(request, f"profile updated successfully")
            return redirect(reverse("profile"))
    else:
        edit_user_form = EditUserForm(
            instance=request.user
        )
        user_profile_form = UserProfileForm(
            instance=request.user.uprofile
        )
    #     print("TEST A")
    #     if UserProfile.objects.filter(user=request.user):
    #         print("TEST B")
    #         print(form.is_valid())
    #         print(formUserProfile.is_valid())
    #         # return redirect('/accounts/profile')
    #     if form.is_valid() and formUserProfile.is_valid():
    #         user = formUserProfile.save()
    #         profile = form.save(commit=False)
    #         request.user = user
    #         profile.save()
    #         print("TEST C")
    #         return redirect('/accounts/profile')
    # else:
    #     if UserProfile.objects.filter(user=request.user):
    #         print("TEST D")
    #         form = EditUserForm(instance=request.user)
    #         formUserProfile = EditUserProfileForm(
    #                           instance=request.user.uprofile)
    #     else:
    #         print("TEST E")
    #         form = EditUserForm(instance=request.user)
    #         formUserProfile = EditUserProfileForm()
    args = {'form': edit_user_form, 'formUserProfile': user_profile_form, 'user': user}
    return render(request, 'update_profile.html', args)


def provider_profile(request, pk=None):
    """The profile of the provider of the book"""
    provider = get_object_or_404(User, pk=pk)
    user_posts = Product.objects.filter(provider_id=provider.id).order_by(
                 '-published_date')
    return render(request, 'profile.html', {"user": provider,
                  'user_posts': user_posts})
