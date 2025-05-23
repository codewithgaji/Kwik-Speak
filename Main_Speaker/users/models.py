from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone                                                                                                                                               

# Create your models here.

# This is the Custom user Manager
class CustomUserManager(BaseUserManager): # This changes some settings from "BaseUserManager"
  def create_user(self, email, password = None, **extra_fields):
    if not email:
      raise ValueError('Users must provide an email address')
    email = self.normalize_email(email) # Puts the email in lowercase etc.
    user = self.model(email=email, **extra_fields) # User object
    user.set_password(password)
    user.save(using=self._db) # Save user to database
    return user
  
  # This is used just like "python manage.py createsuperuser" and saves to 'create_user'
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, password, **extra_fields)
  
class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = CustomUserManager() # This tells Django to use my Custom User manager instead of the models manager

  def __str__(self):
    return self.email