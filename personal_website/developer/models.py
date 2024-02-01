"""
Module containing Django models for the developer app.

Classes:
    Developer

"""

from django.db import models


class Developer(models.Model):

    """
    A class to represent an type of contact with developer.

    Attributes:
        birthday (DateField): Birthday date of developer.
        intro (CharField): Short introduction of developer.
        first_name (CharField): First name of developer.
        last_name (CharField): Last name of developer.
        photo (ImageField): Picture of developer.

    """

    birthday = models.DateField()
    intro = models.CharField(blank=True)
    first_name = models.CharField()
    last_name = models.CharField()
    photo = models.ImageField(blank=True)
