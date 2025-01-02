from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)











