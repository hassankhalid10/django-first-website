# Import the admin module from Django's contrib package to manage the admin interface
from django.contrib import admin

# Import the path function from Django's urls module to define URL patterns
from django.urls import path

# Import views from the home app to handle the logic for the URLs
from home import views

# Define a list of URL patterns for the application
urlpatterns = [
    # Map the root URL (empty string) to the 'index' view in the 'home' app
    path("", views.index, name='home'),
    
    # Map the URL 'about' to the 'about' view in the 'home' app
    path("about", views.about, name='about'),
    
    # Map the URL 'services' to the 'services' view in the 'home' app
    path("services", views.services, name='services'),
    
    # Map the URL 'contact' to the 'contact' view in the 'home' app
    path("contact", views.contact, name='contact'),
]


