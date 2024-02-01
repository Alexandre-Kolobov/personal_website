"""
Registering models with the Django admin.
Registered models can be managed and viewed through the admin interface.

"""

from django.contrib import admin
from .models import Developer

admin.site.register(Developer)
