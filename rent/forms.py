from django import forms
from .models import RentRequest


class RentRequestForm(forms.ModelForm):

    class Meta:
        model = RentRequest
        fields = ('number_of_books', 'username', 'name', 'address', 'book-id')
