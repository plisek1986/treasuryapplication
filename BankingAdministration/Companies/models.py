from django.db import models
from django.urls import reverse
from Accounts.views import COUNTRY_CHOICE


class Company(models.Model):
    """ Class defines attributes for each company object"""

    name = models.CharField(max_length=255, unique=True, blank=False)
    country = models.CharField(max_length=64, choices=COUNTRY_CHOICE)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('Companies:company-list', kwargs=None)
