from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Phone number must be entered in the format: +998xxxxxxxxx'
)


class UserKYCStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'


class User(models.Model):
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password_hash = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserKYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_kyc')

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)

    birth_date = models.DateField()
    address = models.CharField(max_length=128)

    passport_series = models.CharField(max_length=2)
    passport_number = models.CharField(max_length=7)
    pinfl = models.CharField(max_length=14, unique=True)

    status = models.CharField(max_length=100, choices=UserKYCStatus.choices, default=UserKYCStatus.PENDING)

    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)