from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Phone number must be entered in the format: +998xxxxxxxxx'
)

class User(models.Model):
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)


class UserKYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)

    passport_series = models.CharField(max_length=2)
    passport_number = models.CharField(max_length=7)
    pinfl = models.CharField(max_length=14, unique=True)

    birth_date = models.DateField()

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

