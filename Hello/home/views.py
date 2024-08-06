# Import necessary functions and classes from Django and other modules
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Define the view function for the homepage
def index(request):
    # Create a dictionary containing context variables to pass to the template
    context = {
        "variable1": "hassan is great",  # Variable for template rendering
        "variable2": "Rohan is great"    # Another variable for template rendering
    }
    # Render the 'index.html' template with the context variables
    return render(request, 'index.html', context)
    # The following line is commented out, but if active, it would return a simple HttpResponse
    # return HttpResponse("this is homepage")

# Define the view function for the about page
def about(request):
    # Render the 'about.html' template (no context variables needed)
    return render(request, 'about.html')

# Define the view function for the services page
def services(request):
    # Render the 'services.html' template (no context variables needed)
    return render(request, 'services.html')

# Define the view function for the contact page
def contact(request):
    # Check if the request method is POST (form submission)
    if(request.method == "POST"):
        # Get form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # Create a new Contact object with the form data
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        # Save the Contact object to the database
        contact.save()
        # Display a success message to the user
        messages.success(request, 'Your message has been sent!')

    # Render the 'contact.html' template (form submission or not)
    return render(request, 'contact.html')
