"""
Registering models with the Django admin.
Registered models can be managed and viewed through the admin interface.

"""

from django.contrib import admin
from .models import Contact, Experience_pro, Technical_skill, Education, Personal_skill, Interest, Language

admin.site.register(Contact)
admin.site.register(Experience_pro)
admin.site.register(Technical_skill)
admin.site.register(Education)
admin.site.register(Personal_skill)
admin.site.register(Interest)
admin.site.register(Language)
