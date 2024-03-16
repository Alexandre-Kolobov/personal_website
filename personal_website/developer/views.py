"""
Module containing Django views for the developer app.

Functions:
    index
    download_file
"""


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Developer
from resume.models import Contact, \
                          Experience_pro, \
                          Technical_skill, \
                          Education, \
                          Personal_skill, \
                          Interest, \
                          Language

from .forms import ContactForm

import mimetypes
from django.http import FileResponse
from django.core.mail import send_mail
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the index page and manage form

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The HTTP response containing the rendered index page

    """

    developer = Developer.objects.first()
    contacts = Contact.objects.filter(developer=developer)  # same think that developer.contact_set.all() - inverse relation
    experinces_pro = Experience_pro.objects.filter(developer=developer)
    technical_skills = Technical_skill.objects.filter(developer=developer)
    educations = Education.objects.filter(developer=developer)
    personal_skills = Personal_skill.objects.filter(developer=developer)
    interests = Interest.objects.filter(developer=developer)
    languages = Language.objects.filter(developer=developer)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Prise de contact via site CV"
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }

            message = f"Émetteur du message: {body["name"]}\n" \
                      f"Email d'émetteur: {body["email"]}\n" \
                      f"Subject: {body["subject"]}\n" \
                      f"Message: {body["message"]}\n" \

            send_mail(
                subject,
                message,
                'site_cv_alexandre_kolobov@exemple.com',
                ['kolobovalexandre@gmail.com']
                )

            messages.success(request, f'Your message was sent to {developer.first_name} {developer.last_name}')
            return redirect("developer:index")

    else:
        form = ContactForm()

    context = {
        'developer': developer,
        'contacts': contacts,
        'experinces_pro': experinces_pro,
        'technical_skills': technical_skills,
        'educations': educations,
        'personal_skills': personal_skills,
        'interests': interests,
        'languages': languages,
        'form': form,
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
    filename = f"{developer.first_name}_{developer.last_name}_CV.pdf"
    mime_type = mimetypes.guess_type(fl_path)

    return FileResponse(open(fl_path, 'rb'),
                        filename=filename,
                        as_attachment=True,
                        content_type=mime_type,
                        )
