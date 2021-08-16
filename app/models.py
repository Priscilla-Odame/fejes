from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Please set an email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,password = None):
        if not email:
            raise ValueError('Please set your email')
        user = self.create_user(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, email, password = None):
        if not email:
            raise ValueError('Please set your email')
        user = self.create_user(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = False
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=300)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email