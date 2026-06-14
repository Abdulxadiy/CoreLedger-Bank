from django.db import models


class AccountStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    BLOCKED = 'BLOCKED', 'Blocked'
    CLOSED = 'CLOSED', 'Closing'


class Account(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='account')
    account_number = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=100, choices=AccountStatus.choices, default=AccountStatus.ACTIVE)
    balance = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)