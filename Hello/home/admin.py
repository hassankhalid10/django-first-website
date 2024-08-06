# Importing the admin module from Django which provides an interface for managing data.
from django.contrib import admin

# Importing the Contact model from the home application’s models module.
from home.models import Contact

# Register your models here.
# This line registers the Contact model with the Django admin site.
# This allows you to manage the Contact model through the admin interface.
admin.site.register(Contact)

