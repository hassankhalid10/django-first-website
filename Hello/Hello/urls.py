"""Hello URL Configuration

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
# Importing the admin module from Django's contrib package.
from django.contrib import admin

# Importing the path and include functions from Django's urls module.
from django.urls import path, include

# Setting the header text for the admin site.
admin.site.site_header = "hassan Ice Cream Admin"

# Setting the title text for the admin site.
admin.site.site_title = "hassan Ice Cream Admin Portal"

# Setting the index title text for the admin site.
admin.site.index_title = "Welcome to hassan Ice Creams"

# Defining the URL patterns for the project.
urlpatterns = [
    # Mapping the 'admin/' URL path to the admin site URLs.
    path('admin/', admin.site.urls),

    # Including the URL patterns from the 'home' app.
    # This means any URLs defined in 'home/urls.py' will be included here.
    path('', include('home.urls')),
]
