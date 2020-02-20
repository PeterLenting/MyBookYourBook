from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages

# Create your views here. https://wsvincent.com/django-contact-form/


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
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
                          ['FromMyBookYourBook@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,
                             "Thank you for you message! We'll get back to you soon.")
            return redirect(reverse('get_products'))
    return render(request, "contact.html", {'form': form})
