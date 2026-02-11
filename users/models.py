from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from  users.managers import CustomUserManager   
from django.core.exceptions import ValidationError


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    email = models.EmailField(unique=True)
    
    last_login = models.DateTimeField(null=True, blank=True)
    registration_source = models.CharField(max_length=50,default="local")
    phone_number = models.CharField(max_length=20, blank=True,null=True)
    birthdate = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def clean(self):
        if self.is_superuser and not self.phone_number:
            raise ValidationError('The phone number is required for superuser')

    def __str__(self) -> str:
        return self.email

class ConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.email} - {self.code}"