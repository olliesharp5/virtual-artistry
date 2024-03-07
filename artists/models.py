from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
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

    def __str__(self):
        return self.user.username

