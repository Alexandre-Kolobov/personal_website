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
        intro (TextField): Short introduction of developer.
        first_name (CharField): First name of developer.
        last_name (CharField): Last name of developer.
        photo (ImageField): Picture of developer.

    Methods:
        __str__(): Returns a string representation of the profile

    """

    birthday = models.DateField()
    intro = models.TextField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

