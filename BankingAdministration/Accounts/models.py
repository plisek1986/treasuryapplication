from django.db import models
from Users.models import User
from Banks.models import Bank


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
    ('France',  'FR'),  # France
    ('United Kingdom', 'GB'),  # United Kingdom
    ('Greece', 'GR'),  # Greece
    ('Croatia','HR'),  # Croatia
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


class Account(models.Model):
    """ Class defines attributes for each account object"""

    iban_number = models.CharField(max_length=64, unique=True, blank=False, null=False)
    swift_code = models.CharField(max_length=11, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user = models.ManyToManyField(User)


class Company(models.Model):
    pass

