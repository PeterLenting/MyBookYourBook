from django import forms
from .models import Product, UserContact


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'author', 'condition_of_book', 'year_of_edition',
                  'publisher', 'number_of_pages', 'location',
                  'is_for_sale', 'saleprice', 'is_for_rent',
                  'rentprice_per_week', 'image', 'summary')


class UserContactForm(forms.ModelForm):

    class Meta:
        model = UserContact
        fields = ('from_email', 'subject', 'message')
