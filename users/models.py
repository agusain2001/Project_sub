from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    college = models.CharField(max_length=255, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    default_payment_methods = models.JSONField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups",  # Added related_name
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",  # Added related_name
        related_query_name="custom_user",
    )


    def __str__(self):
        return self.username