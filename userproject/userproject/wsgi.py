"""
WSGI config for userproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# Import the 'os' module, which provides a way to interact with the operating system.
import os

# Import the 'get_wsgi_application' function from Django's 'wsgi' module.
# This function is used to create the WSGI application object that Django's server uses.
from django.core.wsgi import get_wsgi_application

# Set the default environment variable 'DJANGO_SETTINGS_MODULE' to 'userproject.settings'.
# This tells Django where to find the settings for the project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userproject.settings')

# Create an instance of the WSGI application using the 'get_wsgi_application' function.
# This instance is used by the WSGI server to communicate with Django and handle requests.
application = get_wsgi_application()

