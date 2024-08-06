from django.apps import AppConfig  # Import the AppConfig class from the django.apps module


class HomeConfig(AppConfig):  # Define a new class called HomeConfig that inherits from AppConfig
    default_auto_field = 'django.db.models.BigAutoField'  # Set the default type for auto-created primary keys to BigAutoField
    name = 'home'  # Specify the name of the application this configuration applies to

