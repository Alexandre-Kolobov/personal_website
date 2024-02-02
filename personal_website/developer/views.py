"""
Module containing Django views for the developer app.

Functions:
    

"""


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Developer


def index(request: HttpRequest) -> HttpResponse:
    developer = Developer.objects.first()
    context = {'developer': developer}

    return render(request, 'index.html', context=context)