from django.db import models
from django.contrib.auth.models import User

CONDITION = ((0, "Excellent"), (1, "Good"), (2, "Worn"))
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Art(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_posts"
    )
    about = models.TextField()
    # image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.DateField()
    condition = models.IntegerField(choices=CONDITION, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Review(models.Model):
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.author}"