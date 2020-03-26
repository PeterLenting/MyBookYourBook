from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here. https://wsvincent.com/django-contact-form/


def emailView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'GET':
            user = User.objects.get(username=request.user.username)
            data = {'from_email': user.email}
            form = ContactForm(initial=data)
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                try:
                    send_mail(subject + " - " + from_email,
                              message,
                              from_email,
                              ['frommybookyourbook@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request,
                                 "Thank you for you message! We'll get back to you soon.")
                return redirect(reverse('get_products'))
        return render(request, "contact.html", {'form': form})
