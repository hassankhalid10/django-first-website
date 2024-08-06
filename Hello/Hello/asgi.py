"""
ASGI config for Hello project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
# Imports the OS module, which provides functions to interact with the operating system

from django.core.asgi import get_asgi_application
# Imports the get_asgi_application function from django.core.asgi. This function sets up the ASGI application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')
# Sets the default value for the DJANGO_SETTINGS_MODULE environment variable. This variable tells Django which settings module to use. Here, 'Hello.settings' is the path to the settings module

application = get_asgi_application()
# Calls the get_asgi_application function to get the ASGI application object. This is the entry point for ASGI-compliant web servers to serve your Django application

