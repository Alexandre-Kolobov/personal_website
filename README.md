![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0-green.svg)
# My Curriculum Vitae Website

This is my personal project to build my own curriculum vitae website. You can visit it by following this URL: [Alexandre Kolobov's CV Website](http://alexandre-kolobov.myddns.me/)

## Project Overview

The project is divided into two parts:

1. **Building a Website Locally**:
   - Backend: Django 5
   - Frontend: HTML, CSS, and JavaScript

2. **Deployment on AWS EC2**:
   - Utilizing Nginx as a WebServer and Gunicorn as the WSGI server for Django

## Local Setup Instructions

To set up the project locally, follow these steps:

1. Ensure you have Python 3.3 or higher installed (verify with `python --version`) along with pip.
   
2. Create a virtual environment:
   - For Windows: `python -m venv venv` (use `venv\Scripts\Activate.ps1` in PowerShell or `source venv/bin/activate` in Bash)
   - For Linux: `python -m venv venv` (`source venv/bin/activate`)
   
3. Clone the repository:
   
   ```bash
   git clone https://github.com/Alexandre-Kolobov/personal_website.git
   cd personal_website

4. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Configure Mailgun:
   - Create a Mailgun account and obtain your personal information.
   - In the `personal_website/personal_website` folder, create a `.env` file and add your Mailgun settings:
   - 
     ```bash
     DEBUG=True
     SECRET_KEY='your_django_secret_key'
     EMAIL_HOST='smtp.mailgun.org'
     EMAIL_PORT='587'
     EMAIL_HOST_USER='postmaster@your_key.mailgun.org'
     EMAIL_HOST_PASSWORD='your_mailgun_password'
     EMAIL_USE_TLS=True

6. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. Create a superuser:
   ```bash
   python manage.py createsuperuser

8. Launch the app locally:
   ```bash
   python manage.py runserver

## Deployment on AWS EC2

For deploying the website on AWS EC2, refer to this tutorial: [Deploying Django, Nginx, and Gunicorn on AWS EC2](https://realpython.com/django-nginx-gunicorn/)
