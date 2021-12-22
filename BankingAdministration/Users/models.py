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
        return self.username
