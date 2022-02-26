from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from model_utils.models import TimeStampedModel


class CustomUser(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=64)
    telegram_id = models.CharField(max_length=64)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
