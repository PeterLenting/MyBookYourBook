from django.conf.urls import url, include
from accounts.views import (index, logout, login, registration, edit_profile,
                            provider_profile, user_profile)
from accounts import url_reset

urlpatterns = [
    url(r'^index/', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^update_profile/$', edit_profile, name="update_profile"),
    url(r'^provider_profile/(?P<pk>\d+)', provider_profile,
        name="provider_profile"),
]
