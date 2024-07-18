from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Añade el argumento related_name a los campos groups y user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Cambia este nombre
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Cambia este nombre
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )

