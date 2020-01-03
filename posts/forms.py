from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'year_of_edition', 'condition_of_book',
                  'publisher', 'number_of_pages', 'provider', 'location',
                  'price', 'image', 'summary')
