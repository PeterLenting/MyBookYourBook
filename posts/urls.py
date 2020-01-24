from django.conf.urls import url
from .views import get_posts, post_detail, delete_post, new_post, edit_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', new_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post'),
]
