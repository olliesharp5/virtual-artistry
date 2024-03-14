from django.db import models

# Create your models here.
class HelpRequest(models.Model):
    """
    This is a HelpRequest model that represents a help request submitted by a user. 

    Attributes:
    name (CharField): The name of the user, requiring a maximum of 200 characters. 
    email (EmailField): The user's email address.
    message (TextField): An open text field used to hold the user's help request message.
    created_at (DateTimeField): The date and time when the help request was created, automatically set when the object is first created.

    Methods:
    __str__(): Returns a readable string representation of the HelpRequest object, in this case, the user's name who made the request.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Help request from {self.name}"