from django.conf.urls import url
from .views import about_view

urlpatterns = [
    url(r'^about/', about_view, name="about"),
]
