from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A single post
    Title, author, year of print, condition of book, provider, location,
    publisher, number of pages, sell, rent, price, summary
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_of_edition = models.CharField(max_length=4)
    condition_of_book = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    number_of_pages = models.CharField(max_length=4)
    price = models.CharField(max_length=200)
    summary = models.TextField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title
