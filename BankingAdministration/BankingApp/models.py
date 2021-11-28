from django.db import models
from django.contrib.auth.models import AbstractUser


# we create User from AbstractUser to allow us for changes to a predefined model of Django User, in case those are
# needed in the future
class User(AbstractUser):
    pass
