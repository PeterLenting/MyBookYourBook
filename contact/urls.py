from django.conf.urls import url
from .views import emailView, successView

urlpatterns = [
    url(r'^$', emailView, name='contact'),
    url(r'^success/', successView, name='success'),
]
