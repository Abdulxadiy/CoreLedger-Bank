from django.db import models


class Type(models.TextChoices):
    DEPOSIT = 'DEPOSIT', 'Deposit'
    WITHDRAW = 'WITHDRAW', 'Withdraw'
    TRANSFER = 'TRANSFER', 'Transfer'


class TransactionStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'
    REVERSED = 'REVERSED', 'Reversed'


class Transaction(models.Model):
    reference = models.CharField(max_length=200, unique=True)
    sender_account = models.ForeignKey('Account', on_delete=models.PROTECT, related_name='sender_account')
    receiver_account = models.ForeignKey('Account', on_delete=models.PROTECT, related_name='receiver_account')
    amount = models.BigIntegerField()
    type = models.CharField(max_length=10, choices=Type.choices)
    source = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=TransactionStatus.choices, default=TransactionStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)


