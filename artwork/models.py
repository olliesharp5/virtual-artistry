from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from artists.models import ArtistProfile

CONDITION = ((0, "Excellent"), (1, "Good"), (2, "Worn"))
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Art(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    artist = models.ForeignKey(
        ArtistProfile, on_delete=models.CASCADE, related_name="art_posts"
    )
    about = models.TextField()
    art_image = CloudinaryField('art_image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.DateField()
    condition = models.IntegerField(choices=CONDITION, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of artwork post is {self.title}"


class Review(models.Model):
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"