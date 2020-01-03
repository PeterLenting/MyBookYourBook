from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'condition_of_book', 'year_of_edition',
                  'publisher', 'number_of_pages', 'provider', 'location',
                  'price', 'image', 'summary')
