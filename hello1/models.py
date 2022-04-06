from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager,UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here
# This class inherit basemanager
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        user=self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
     # This function for the user creation and we don't need give permission and superuser and staff
    def create_user(self, email, password, first_name, last_name,mobile, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name,mobile, **extra_fields)
    
    
# This function for creating superuser and we should give the permissin of sueruser and staff
    def create_superuser(self, email, password, first_name, last_name,mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name,mobile, **extra_fields)
        

# The purpose of this model is to change login field means we change username field at the replacement of email  

class User(AbstractBaseUser,PermissionsMixin):
      # AbstractBaseUser has password,last_login,is_active by default
      
      email=models.EmailField(db_index=True,unique=True,max_length=254)  # Email should be unique
      first_name=models.CharField(max_length=150)
      last_name=models.CharField(max_length=150)
      mobile=models.CharField(max_length=40)
      address=models.CharField(max_length=350)
      
      is_staff=models.BooleanField(default=False)   # it must be needed
      is_active=models.BooleanField(default=True)
      is_superuser=models.BooleanField(default=False)
      
      objects = CustomUserManager()

      USERNAME_FIELD = 'email'                      # it must be needed to change usernamefield
      REQUIRED_FIELDS = ['first_name','last_name','mobile']
      
      class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

# This model is created table for our product data
class Product(models.Model):
    name=models.CharField(max_length=50)
    auth_name=models.CharField(max_length=50)
    price=models.IntegerField(default=250)
    description=models.CharField(max_length=800,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')