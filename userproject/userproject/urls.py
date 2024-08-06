"""userproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import the admin module from Django's contrib package
from django.contrib import admin

# Import the path and include functions from Django's urls module
from django.urls import path, include

# Define a list of URL patterns for the project
urlpatterns = [
    # Route for the admin interface, handled by Django's admin site
    path('admin/', admin.site.urls),
    
    # Route for the root URL, including URL patterns from the 'home' app
    path('', include('home.urls')),
]

