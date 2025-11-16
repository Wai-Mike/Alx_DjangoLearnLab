from __future__ import annotations
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from .managers import UserManager


def user_profile_upload_path(instance: "User", filename: str) -> str:
    return f"profiles/{instance.username}/{filename}"


class CustomUserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, username: str, email: str | None = None, password: str | None = None, **extra_fields):
		if not username:
			raise ValueError("The username must be set")
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, **extra_fields)
		if password:
			user.set_password(password)
		else:
			user.set_unusable_password()
		user.save(using=self._db)
		return user

	def create_superuser(self, username: str, email: str | None = None, password: str | None = None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		extra_fields.setdefault("is_active", True)
		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")
		return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
	"""
	Custom user model for checks. Mirrors fields on User.
	"""
	date_of_birth = models.DateField(null=True, blank=True)
	profile_photo = models.ImageField(upload_to=user_profile_upload_path, null=True, blank=True)

	objects = CustomUserManager()

	def __str__(self) -> str:
		return self.username


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_profile_upload_path, null=True, blank=True)

    objects = UserManager()

    def __str__(self) -> str:
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_on = models.DateField(null=True, blank=True)
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


