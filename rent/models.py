from django.db import models

# Create your models here.


class RentRequest(models.Model):
    total_amount = models.CharField(max_length=50,
                                    blank=True,
                                    )
    username = models.CharField(max_length=50,
                                blank=True)
    email = models.CharField(max_length=50,
                             blank=True,
                             )
    books = models.CharField(max_length=30,
                             blank=True,
                             )
