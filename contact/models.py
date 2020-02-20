from django.db import models

# Create your models here.


class Contact(models.Model):
    from_email = models.EmailField(null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=500, null=True)
