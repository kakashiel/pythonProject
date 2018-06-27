from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    phone = models.CharField(max_length=17, blank=True)
    reasonOnTheSite = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.email
