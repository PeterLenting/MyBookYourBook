from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="uprofile")
    location = models.CharField(max_length=30, blank=True)
    want_to_rent = models.BooleanField(
                   "I want to be able to rent books*",
                   default=False)
    have_paid = models.BooleanField(
                "I have paid my deposite",
                default=False,
                blank=True)

    def __str__(self):
        return self.user.username
