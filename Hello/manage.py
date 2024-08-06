#!/usr/bin/env python
# This shebang line allows the script to be run directly from the command line.
# It specifies that the script should be executed using the Python interpreter.

"""Django's command-line utility for administrative tasks."""
# This is a docstring that describes the purpose of this script. It is used for administrative tasks in Django.

import os
import sys
# Importing the 'os' and 'sys' modules. 'os' provides a way to interact with the operating system, and 'sys' provides access to system-specific parameters and functions.

def main():
    """Run administrative tasks."""
    # This is the main function that will be executed when the script runs.

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')
    # Set the default value for the environment variable 'DJANGO_SETTINGS_MODULE' to 'Hello.settings'.
    # This tells Django which settings module to use for this project.

    try:
        from django.core.management import execute_from_command_line
        # Try to import the 'execute_from_command_line' function from Django's management module.
        # This function allows Django to execute commands passed on the command line.
    except ImportError as exc:
        # If the import fails, handle the ImportError exception.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # Raise a custom ImportError message with details if Django is not installed or the virtual environment is not activated.

    execute_from_command_line(sys.argv)
    # Call the 'execute_from_command_line' function with 'sys.argv', which contains the command line arguments passed to the script.

if __name__ == '__main__':
    main()
    # If this script is run directly (not imported as a module), call the 'main' function.
