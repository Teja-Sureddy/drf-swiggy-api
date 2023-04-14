from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from .models_list.role import Role


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username required')
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        role, created = Role.objects.get_or_create(name='admin')
        if role:
            extra_fields.setdefault('role', role)
        else:
            extra_fields.setdefault('role', created)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True,max_length=255,blank=False)
    email = models.EmailField(unique=True,max_length=255,blank=False)
    is_staff = models.BooleanField('staff status',default=False)
    is_active = models.BooleanField('active',default=False)
    is_superuser = models.BooleanField('superuser',default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
  
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username