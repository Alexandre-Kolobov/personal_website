"""
Module containing Django models for the developer app.

Classes:
    Developer

"""

from django.db import models
from PIL import Image
import os
from django.conf import settings


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
        save(): Overwrite save method to include image resizing
        delete(): Overwrite delete method to include image removing when model is removed

    """

    birthday = models.DateField()
    intro = models.TextField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    role = models.CharField(max_length=100, null=True)
    cv_file = models.FileField(upload_to="uploads/", blank=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.photo))
            img = Image.open(file_path)
            target_size = (444, 562)
            img.thumbnail(target_size, Image.LANCZOS)
            img.save(self.photo.path)

        super().save(*args, **kwargs)

    def delete(self):
        if self.photo:
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.photo))
            if os.path.exists(file_path):
                os.remove(file_path)
        return super().delete()