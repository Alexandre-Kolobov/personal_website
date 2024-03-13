"""
Module containing Django views for the developer app.

Functions:
    index
    download_file
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

import mimetypes
from urllib.request import urlopen
from django.conf import settings
from django.http import FileResponse


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

def download_file(request: HttpRequest) -> FileResponse:
    """
    Download a file from the server.

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        FileResponse: The response containing the file to download.

    """

    developer = Developer.objects.first()
    fl_path = developer.cv_file.path
    filename = "Alexandre_Kolobov_CV"
   
    mime_type, _ = mimetypes.guess_type(fl_path)

    return FileResponse(open(fl_path,'rb'),
                        filename=filename,
                        as_attachment=True,
                        content_type=mime_type,
                        )
