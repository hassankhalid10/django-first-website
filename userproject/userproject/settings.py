"""
Django settings for userproject project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os  # Import the OS module for interacting with the operating system
from pathlib import Path  # Import Path for easier path manipulations

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Define the base directory of the project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4g$y4q5a#ug3o2txa0h9imav391evdu3vy3u79@2zri0g48djo'  # Secret key for cryptographic operations, should be kept secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Enable or disable debug mode; should be False in production

ALLOWED_HOSTS = ['codewithhassan.com', 'programmingwithhassan.com', '127.0.0.1']  # List of allowed host/domain names for this site

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin app for managing the site
    'django.contrib.auth',  # Django authentication framework
    'django.contrib.contenttypes',  # Django content types framework
    'django.contrib.sessions',  # Django sessions framework
    'django.contrib.messages',  # Django messaging framework
    'django.contrib.staticfiles',  # Django static files management
    'home',  # Custom application 'home' that you have created
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware for security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware for managing sessions
    'django.middleware.common.CommonMiddleware',  # Common middleware for handling things like ETag headers
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware for Cross-Site Request Forgery protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware for user authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware for handling messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware for clickjacking protection
]

ROOT_URLCONF = 'userproject.urls'  # The module where URL patterns are defined

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend used for rendering templates
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # Directories where Django will look for templates
        'APP_DIRS': True,  # Whether to look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Adds debugging information to templates
                'django.template.context_processors.request',  # Adds request context to templates
                'django.contrib.auth.context_processors.auth',  # Adds user authentication context
                'django.contrib.messages.context_processors.messages',  # Adds messaging context
            ],
        },
    },
]

WSGI_APPLICATION = 'userproject.wsgi.application'  # WSGI application callable used by the server to run the project

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database backend to use (SQLite in this case)
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the SQLite database file
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validator for user attribute similarity
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validator for minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validator for common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validator for numeric passwords
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # Language code for the site

TIME_ZONE = 'UTC'  # Time zone for the site

USE_I18N = True  # Whether to enable internationalization (i18n) support

USE_TZ = True  # Whether to enable timezone support

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'  # URL to use when referring to static files

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default type for auto-generated primary keys

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Additional directories to look for static files
]
