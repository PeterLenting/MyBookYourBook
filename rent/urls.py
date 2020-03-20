from django.conf.urls import url
from .views import rent_view, rent_success_view

urlpatterns = [
    url(r'^$', rent_view, name='rent'),
    url(r'^rent_success/', rent_success_view, name='rent_success'),
]
