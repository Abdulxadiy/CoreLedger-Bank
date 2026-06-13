from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Phone number must be entered in the format: +998xxxxxxxxx'
)

class User(models.Model):
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password_hash = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserKYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)

    birth_date = models.DateField()
    address = models.CharField(max_length=128)

    passport_series = models.CharField(max_length=2)
    passport_number = models.CharField(max_length=7)
    pinfl = models.CharField(max_length=14, unique=True)

    status = models.CharField(max_length=100, default='pending')

    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)


class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=150, unique=True)
    level = models.PositiveIntegerField()
    permissions = models.ManyToManyField(Permission, related_name='roles')
    description = models.TextField()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_number = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=128)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)




