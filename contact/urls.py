from django.contrib import admin
from django.conf.urls import url
from .views import emailView, successView

urlpatterns = [
    url(r'^contact/', emailView, name='contact'),
    url(r'^success/', successView, name='success'),
]
