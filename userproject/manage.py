#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# This is the shebang line that tells the system to use the Python interpreter to run this script.
# The docstring explains that this script is for running administrative tasks in Django.

import os
import sys
# Import the `os` and `sys` modules. `os` is used for interacting with the operating system,
# and `sys` is used for interacting with the Python runtime environment.

def main():
    """Run administrative tasks."""
    # This function will run administrative tasks related to Django.
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userproject.settings')
    # Set the default value for the environment variable 'DJANGO_SETTINGS_MODULE' to 'userproject.settings'.
    # This tells Django which settings module to use. 

    try:
        from django.core.management import execute_from_command_line
        # Attempt to import the `execute_from_command_line` function from Django's management module.
        # This function is used to execute commands passed from the command line.

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # If the import fails, raise an ImportError with a descriptive message.
        # This error message helps diagnose if Django is not installed or if the virtual environment is not activated.

    execute_from_command_line(sys.argv)
    # Call the `execute_from_command_line` function with the command-line arguments passed to the script.
    # This executes the Django management commands provided.

if __name__ == '__main__':
    main()
    # If this script is being run as the main program, call the `main()` function to execute administrative tasks.

