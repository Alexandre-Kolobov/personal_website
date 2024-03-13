"""
URLs for developer application
"""


from . import views
from django.urls import path

app_name = "developer"

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.download_file, name='download_file'),
]
