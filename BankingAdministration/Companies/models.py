from django.db import models
from django.urls import reverse

# from Accounts.models import COUNTRY_CHOICE

COUNTRY_CHOICE = [
    ('Austria', 'AT'),  # Austria
    ('Belgium', 'BE'),  # Belgium
    ('Bulgaria', 'BG'),  # Bulgaria
    ('Switzerland', 'CH'),  # Switzerland
    ('Czech Republic', 'CZ'),  # Czech Republic
    ('Germany', 'DE'),  # Germany
    ('Denmark', 'DK'),  # Denmark
    ('Estonia', 'EE'),  # Estonia
    ('Spain', 'ES'),  # Spain
    ('Finland', 'FI'),  # Finland
    ('France', 'FR'),  # France
    ('United Kingdom', 'GB'),  # United Kingdom
    ('Greece', 'GR'),  # Greece
    ('Croatia', 'HR'),  # Croatia
    ('Hungary', 'HU'),  # Hungary
    ('Ireland', 'IE'),  # Ireland
    ('Iceland', 'IS'),  # Iceland
    ('Italy', 'IT'),  # Italy
    ('Kazakhstan', 'KZ'),  # Kazakhstan
    ('Lithuania', 'LT'),  # Lithuania
    ('Latvia', 'LV'),  # Latvia
    ('Netherlands', 'NL'),  # Netherlands
    ('Norway', 'NO'),  # Norway
    ('Poland', 'PL'),  # Poland
    ('Portugal', 'PT'),  # Portugal
    ('Romania', 'RO'),  # Romania
    ('Sweden', 'SE'),  # Sweden
    ('Slovenia', 'SI'),  # Slovenia
    ('Slovakia', 'SK'),  # Slovakia
    ('Turkey', 'TR'),  # Turkey
]


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
