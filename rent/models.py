from django.db import models

# Create your models here.


class RentRequest(models.Model):
    total_amount = models.DecimalField(max_length=20,
                                       decimal_places=2,
                                       max_digits=10,
                                       blank=True,
                                       null=True
                                       )
    username = models.CharField(max_length=50,
                                blank=True,
                                null=True)
    email = models.CharField(max_length=50,
                             blank=True,
                             null=True
                             )
    books = models.CharField(max_length=30,
                             blank=True,
                             null=True
                             )
