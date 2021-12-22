from django.db import models
from django.contrib.auth.models import AbstractUser


# we create User from AbstractUser to allow us for changes to a predefined model of Django User, in case those are
# needed in the future
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    is_payment_creator = models.BooleanField(default=False)
    is_payment_approver = models.BooleanField(default=False)
    can_delete_payment = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = 'Users'

    def __str__(self):
        return self


# class Account(models.Model):
#     """ Class defines attributes for each account object"""
#
#     iban_number = models.CharField(max_length=64, unique=True, blank=False, null=False)
#     swift_code = models.CharField(max_length=11, blank=False)
#     bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
#     company = models.ForeignKey('Company', on_delete=models.CASCADE)
#     user = models.ManyToManyField(User)
#
#     def __str__(self):
#         return self
#
#
# class Bank(models.Model):
#     pass
#
#
# class Company(models.Model):
#     pass
