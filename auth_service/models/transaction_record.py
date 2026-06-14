from rest_framework.exceptions import ValidationError
from django.db import models


class EntryType(models.TextChoices):
    DEBIT = 'DEBIT', 'Debit'
    CREDIT = 'CREDIT', 'Credit'


class TransactionRecord(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.PROTECT, related_name='records')
    account = models.ForeignKey('Account', on_delete=models.PROTECT, related_name='records')
    entry_type = models.CharField(max_length=10, choices=EntryType.choices)
    amount = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError('Amount must be greater than 0')

