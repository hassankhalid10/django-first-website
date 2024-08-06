# Import necessary functions and classes from Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Note: The password for the test user 'hassan' is hassan$$$***000

# Define the view function for the homepage
def index(request):
    # Check if the user is not logged in (anonymous)
    if request.user.is_anonymous:
        # Redirect to the login page if the user is not logged in
        return redirect("/login")
    # Render and return the 'index.html' template if the user is logged in
    return render(request, 'index.html')

# Define the view function for logging in a user
def loginUser(request):
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Retrieve username and password from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the user with the provided credentials
        user = authenticate(username=username, password=password)
        # Check if authentication was successful
        if user is not None:
            # Log the user in and redirect to the homepage
            login(request, user)
            return redirect("/")
        else:
            # If authentication fails, render the 'login.html' template again
            return render(request, 'login.html')
    # If request method is not POST, render the 'login.html' template
    return render(request, 'login.html')

# Define the view function for logging out a user
def logoutUser(request):
    # Log out the current user
    logout(request)
    # Redirect to the login page after logging out
    return redirect("/login")
