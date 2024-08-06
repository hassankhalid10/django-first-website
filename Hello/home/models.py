from django.db import models  # Import the models module from Django's database package

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):  # Define a new model called Contact, inheriting from Django's Model class
    name = models.CharField(max_length=122)  # Create a CharField for the name, with a maximum length of 122 characters
    email = models.CharField(max_length=122)  # Create a CharField for the email, with a maximum length of 122 characters
    phone = models.CharField(max_length=12)  # Create a CharField for the phone number, with a maximum length of 12 characters
    desc = models.TextField()  # Create a TextField for a description; TextField can hold a large amount of text
    date = models.DateField()  # Create a DateField to store date information

    def __str__(self):  # Define the string representation of the model
        return self.name  # Return the name field when the model is converted to a string

