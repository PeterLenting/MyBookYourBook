from django.conf.urls import url

urlpatterns = [
    url(r'^$', emailView, name='contact'),
]
