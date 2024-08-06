# Import the AppConfig class from the django.apps module
from django.apps import AppConfig

# Define a new configuration class for the 'home' app
class HomeConfig(AppConfig):
    # Set the default type for auto-created primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the name of the app configuration
    name = 'home'

