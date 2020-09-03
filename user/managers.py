from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an Email Address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('staff', False)
        extra_fields.setdefault('admin', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('staff', True)
        extra_fields.setdefault('admin', True)

        if extra_fields.get('staff') is not True:
            raise ValueError('Superuser must have "staff" = True')
        if extra_fields.get('admin') is not True:
            raise ValueError('Superuser must have "admin" = True')
        return self._create_user(email, password, **extra_fields)
