"""
WSGI config for Hello project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os  # Import the os module, which provides functions to interact with the operating system

from django.core.wsgi import get_wsgi_application  # Import the get_wsgi_application function from Django's core WSGI module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')  
# Set the default settings module for the Django project to 'Hello.settings'
# This tells Django where to find the settings for the project

application = get_wsgi_application()  
# Create a WSGI application object that Django can use to communicate with the web server
# This application object is used by the server to forward requests to and receive responses from Django

