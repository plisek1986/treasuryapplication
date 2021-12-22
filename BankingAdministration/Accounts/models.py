from django.db import models
from Users.models import User


class Account(models.Model):
    """ Class defines attributes for each account object"""

    iban_number = models.CharField(max_length=64, unique=True, blank=False, null=False)
    swift_code = models.CharField(max_length=11, blank=False)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user = models.ManyToManyField('Users.User')


class Bank(models.Model):
    pass


class Company(models.Model):
    pass

