from django.conf.urls import url
from .views import (get_products, product_detail, delete_product, new_product,
                    edit_product, get_rent_products, get_sale_products,
                    user_contact_form_view, get_my_products)
from cart.views import remove_item

urlpatterns = [
    url(r'^$', get_products, name='get_products'),
    url(r'^my_products/$', get_my_products, name='get_my_products'),
    url(r'^products_for_rent/$', get_rent_products, name='get_rent_products'),
    url(r'^products_for_sale/$', get_sale_products, name='get_sale_products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^new/$', new_product, name='new_product'),
    url(r'^(?P<pk>\d+)/edit/$', edit_product, name='edit_product'),
    url(r'^(?P<pk>\d+)/delete/$', delete_product, name='delete_product'),
    url(r'^remove/', remove_item, name='remove'),
    url(r'^(?P<pk>\d+)/usercontactpage/$', user_contact_form_view, name='user_contact_page')
]
