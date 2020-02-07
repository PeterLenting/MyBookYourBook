from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="uprofile")
    location = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
