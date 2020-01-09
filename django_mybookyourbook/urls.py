"""MyBookYourBook URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts.views import index, logout, login, registration, user_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^accounts/index/$', index, name="index"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', user_profile, name="profile"),
]
"""
    TIJDELIJK UITGESCHAKELD OM INDEX.html te kunnen bouwen met accounts. Hierdoor werkt /posts/ niet
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
"""
