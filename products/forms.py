from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'author', 'condition_of_book', 'year_of_edition',
                  'publisher', 'number_of_pages', 'location',
                  'is_for_sale', 'saleprice', 'is_for_rent',
                  'rentprice_per_week', 'image', 'summary')
        error_messages = {
            'is_for_rent': {
                'required': ("Hey yow! this field is required!")
            }
        }
