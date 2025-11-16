from __future__ import annotations
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


def user_profile_upload_path(instance: "User", filename: str) -> str:
    return f"profiles/{instance.username}/{filename}"


class CustomUser(AbstractUser):
    """
    Mirrored custom user model for path-based checks.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_profile_upload_path, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_profile_upload_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_on = models.DateField(null=True, blank=True)
    # Kept for parity with the primary app model; not required for the check
    created_by = models.ForeignKey("bookshelf.User", on_delete=models.CASCADE, related_name="books")

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self) -> str:
        return self.title


