from django.db import models

# Create your models here.


class RentRequest(models.Model):
    number_of_books = models.CharField(max_length=50,
                                       blank=False)
    username = models.CharField(max_length=50,
                                blank=False,
                                default="{{ request.user }}")
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    book_id = models.CharField(max_length=30, blank=False)
