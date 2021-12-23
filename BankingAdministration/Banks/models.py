from django.db import models


class Bank(models.Model):
    """ Class defines attributes for each bank object"""

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name
