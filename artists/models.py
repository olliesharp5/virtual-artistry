from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    """
    This is a UserProfile model that represents an extended user profile.

    Attributes:
    USER_ROLES (tuple): A tuple constant that defines the possible roles ('RU', 'Regular User'), ('AR', 'Artist'), and ('AD', 'Admin') that a user can have in the system.
    user (OneToOneField): A one-to-one relationship with the User model; on user deletion, the associated profile will also be deleted.
    role (CharField): The role of the user within the application. Choices are defined in the USER_ROLES constant, with 'Regular User' as default.
    display_name (CharField): The displayed name for the user in the system. It can be null and unique with a maximum of 100 characters.
    location (TextField): The recorded location for the user.
    profile_image (CloudinaryField): The profile image of the user, with a default placeholder when no image is provided.
    about (TextField): A text describing about the user.

    Methods:
    is_artist(): Checks if the user is an artist, returns True if the user's role is 'Artist', otherwise returns False.
    __str__(): Returns a readable string representation of the UserProfile object, indicating the username of the user.
    """
    USER_ROLES = (
        ('RU', 'Regular User'),
        ('AR', 'Artist'),
        ('AD', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, default="1")
    role = models.CharField(max_length=2, choices=USER_ROLES, default='RU')
    display_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    location = models.TextField()
    profile_image = CloudinaryField('profile_image', default='profile_placeholder')
    about = models.TextField()

    def is_artist(self):
        return self.role == 'AR'

    def __str__(self):
        return self.user.username

