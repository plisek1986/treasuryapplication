from django.db import models
from django.contrib.auth.models import AbstractUser


# we create User from AbstractUser to allow us for changes to a predefined model of Django User, in case those are
# needed in the future
class User(AbstractUser):
    internal_id = models.CharField(max_length=7, blank=False, null=False, default='ID')
    account = models.ManyToManyField('Account')
    is_administrator = models.BooleanField(default=False)
    is_payment_creator = models.BooleanField(default=False)
    is_payment_approver = models.BooleanField(default=False)
    can_delete_payment = models.BooleanField(default=False)
    access = models.ManyToManyField('Access')


class Account(models.Model):
    pass


class Access(models.Model):
    pass
