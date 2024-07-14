from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)







