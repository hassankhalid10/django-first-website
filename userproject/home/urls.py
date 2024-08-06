# Import the admin module from Django's contrib package
from django.contrib import admin

# Import path and include functions from Django's urls module
from django.urls import path, include

# Import views from the home app
from home import views

# Define the URL patterns for your application
urlpatterns = [
    # Map the root URL ('') to the index view from the home app and name this URL pattern 'home'
    path('', views.index, name="home"),

    # Map the URL 'login' to the loginUser view from the home app and name this URL pattern 'login'
    path('login', views.loginUser, name="login"),

    # Map the URL 'logout' to the logoutUser view from the home app and name this URL pattern 'logout'
    path('logout', views.logoutUser, name="logout"),
]
