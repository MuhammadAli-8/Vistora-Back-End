from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin'),
    ]
    # add additional fields in here
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=255, default='Customer', choices=ROLE_CHOICES)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.is_staff and not self.role == "Staff":
            self.role = "Staff"
        if self.is_superuser and not self.role == "Admin":
            self.role = "Admin"
        super().save(*args, **kwargs)


