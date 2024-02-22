from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtistProfile(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
  # profile_image = CloudinaryField('image', default='placeholder')
    about = models.TextField()

    def __str__(self):
        return self.name
