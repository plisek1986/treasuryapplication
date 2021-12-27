from django.db import models
from django.shortcuts import reverse


class Bank(models.Model):
    """ Class defines attributes for each bank object"""

    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('Banks:bank-list', kwargs=None)
