from django.conf.urls import url
from .views import rent_view

urlpatterns = [
    url(r'^$', rent_view, name='rent'),
]
