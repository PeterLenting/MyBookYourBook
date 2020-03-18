from django import forms
from .models import RentRequest


class RentRequestForm(forms.ModelForm):

    class Meta:
        model = RentRequest
        fields = ('total_amount', 'username', 'email', 'books')
