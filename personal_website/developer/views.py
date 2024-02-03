"""
Module containing Django views for the developer app.

Functions:
    index

"""


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Developer
from resume.models import Contact,\
                          Experience_pro,\
                          Technical_skill,\
                          Education,\
                          Personal_skill,\
                          Interest,\
                          Language


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the index page

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered index page

    """

    developer = Developer.objects.first()
    contacts = Contact.objects.filter(developer=developer) #same think that developer.contact_set.all() - inverse relation 
    experinces_pro = Experience_pro.objects.filter(developer=developer)
    technical_skills = Technical_skill.objects.filter(developer=developer)
    educations = Education.objects.filter(developer=developer)
    personal_skills = Personal_skill.objects.filter(developer=developer)
    interests = Interest.objects.filter(developer=developer)
    languages = Language.objects.filter(developer=developer)

    context = {
        'developer': developer,
        'contacts': contacts,
        'experinces_pro': experinces_pro,
        'technical_skills': technical_skills,
        'educations': educations,
        'personal_skills': personal_skills,
        'interests': interests,
        'languages': languages,
        }

    return render(request, 'index.html', context=context)