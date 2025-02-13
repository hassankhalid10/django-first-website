"""
Django settings for Hello project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
# Importing the os module for interacting with the operating system.
import os

# Importing Path from pathlib module to work with file paths.
from pathlib import Path

# Importing constants from django.contrib.messages to customize message tags.
from django.contrib.messages import constants as messages

# Defining the base directory of the project, which is the parent directory of the current file's directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# Setting for quick-start development, which is not suitable for production environments.
# See the deployment checklist at https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# WARNING: Keep the secret key used in production secret to ensure security.
SECRET_KEY = 'django-insecure-np$&06)#3#h7ney&ongb_7qyakpua*=f4$qjf_+jm$7i4&v3*n'

# WARNING: Debug mode should be turned off in production to avoid security risks.
DEBUG = True

# Defining the hosts/domain names that this Django site can serve.
ALLOWED_HOSTS = []

# Application definition section where installed apps, middleware, URL configurations, and templates are defined.
INSTALLED_APPS = [
    'django.contrib.admin',              # Admin site app
    'django.contrib.auth',               # Authentication framework
    'django.contrib.contenttypes',       # Content types framework
    'django.contrib.sessions',           # Session framework
    'django.contrib.messages',           # Messaging framework
    'django.contrib.staticfiles',        # Static file handling
    'home',                              # Custom app named 'home'
]

# List of middleware to be used by the project.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',                    # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',              # Session middleware
    'django.middleware.common.CommonMiddleware',                         # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',                         # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',           # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',              # Messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',            # Clickjacking protection middleware
]

# Root URL configuration module for the project.
ROOT_URLCONF = 'Hello.urls'

# Template configuration section.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend engine for Django templates
        'DIRS': [os.path.join(BASE_DIR, "templates")],                 # Directories where templates are stored
        'APP_DIRS': True,                                              # Enable loading templates from installed apps
        'OPTIONS': {                                                   # Template options
            'context_processors': [                                    # Context processors used in templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application configuration for deploying the project.
WSGI_APPLICATION = 'Hello.wsgi.application'

# Database configuration section. Default database is SQLite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',       # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',              # Database file location
    }
}

# Password validation settings.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Checks similarity to user attributes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',            # Ensures minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',           # Prevents common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',          # Prevents fully numeric passwords
    },
]

# Internationalization settings.
LANGUAGE_CODE = 'en-us'   # Language code

TIME_ZONE = 'UTC'         # Time zone

USE_I18N = True           # Enable internationalization

USE_TZ = True             # Enable time zone support

# Static files configuration (CSS, JavaScript, Images).
STATIC_URL = '/static/'   # URL to use when referring to static files

# Default primary key field type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'   # Default field type for primary keys

# Additional static files directories.
STATICFILES_DIRS = [
    BASE_DIR / "static",   # Directory for static files
]


