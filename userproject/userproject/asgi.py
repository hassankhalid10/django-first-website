"""
ASGI config for userproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# Import the os module, which provides a way to interact with the operating system
import os

# Import the get_asgi_application function from Django's core ASGI module
from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to point to your project's settings
# This tells Django which settings module to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userproject.settings')

# Create an ASGI application callable that Django's ASGI server will use to handle requests
application = get_asgi_application()

