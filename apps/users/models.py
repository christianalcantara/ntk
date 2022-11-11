from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=timezone.now(),
            registered_at=timezone.now(),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop("is_staff", False)
        is_superuser = extra_fields.pop("is_superuser", False)
        return self._create_user(
            email, password, is_staff, is_superuser, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("Email"), unique=True, max_length=255)
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=30, default="first"
    )
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=30, default="last"
    )
    avatar = models.ImageField(verbose_name=_("Avatar"), blank=True)

    is_admin = models.BooleanField(verbose_name=_("Admin"), default=False)
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)
    is_customer = models.BooleanField(verbose_name=_("Customer"), default=False)
    is_staff = models.BooleanField(verbose_name=_("Staff"), default=False)
    registered_at = models.DateTimeField(
        verbose_name=_("Registered at"), auto_now_add=timezone.now
    )
    # Fields settings
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.fget.short_description = _("Full name")

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}."

    short_name.fget.short_description = _("Short name")

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """post_save signal to generate token automatically"""
    if created:
        Token.objects.create(user=instance)
