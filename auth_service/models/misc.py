from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='employees')
    employee_number = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=128)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL, related_name='employees')
    is_active = models.BooleanField(default=True)


class Card(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16, unique=True)
    expire_date = models.DateField()


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)