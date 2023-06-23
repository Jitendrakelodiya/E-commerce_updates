from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# from django.contrib.auth.models import PermissionMixin




  
class User(AbstractUser):
     

      user_choice = [
        ('seller', 'seller'),
        ('buyer', 'buyer'),
      ]
    
      username = models.CharField(max_length=150, unique=True, blank=True, null=True)
      email = models.EmailField(unique=True)
      mobile = models.CharField(max_length=10)
      user_type = models.CharField(max_length=6, choices=user_choice,default='buyer')



      objects = CustomUserManager()
 
      # USERNAME_FIELD = 'email'
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []
  

