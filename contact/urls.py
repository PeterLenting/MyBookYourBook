from django.conf.urls import url
from .views import emailView

urlpatterns = [
    url(r'^$', emailView, name='contact'),
]
