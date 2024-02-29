from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class ArtistProfile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.TextField()
    artist_image = CloudinaryField('artist_image', default='placeholder')
    about = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
