import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from artists.models import UserProfile

CONDITION = ((0, "Excellent"), (1, "Good"), (2, "Worn"))
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Art(models.Model):
    """
    This is an Art model that represents a piece of art posted by a user.

    Attributes:
    title (CharField): The title of the art, requiring a maximum of 100 characters and it has to be unique.
    slug (SlugField): The slug for the art post, also requiring a maximum of 100 characters and has to be unique.
    artist (ForeignKey): The profile of the user who posted the art. On user deletion, all their art posts will be deleted.
    about (TextField): A text description about the art.
    art_image (CloudinaryField): The image of the art post, with a default placeholder when no image is provided.
    price (DecimalField): The price of the art, with a maximum of 10 digits and 2 decimal places.
    year (PositiveIntegerField): The year the art was created; values should fall between 1600 and the current year.
    condition (IntegerField): The condition of the artwork, defaulted to 0. Choices are defined in CONDITION.
    created_on (DateTimeField): The date and time when the art was posted, automatically set when the object is first created.
    status (IntegerField): The status of the artwork, defaulted to 0. Choices are defined in STATUS.

    Meta:
    The artwork posts are ordered by their creation date in descending order.

    Methods:
    __str__(): Returns a readable string representation of the Art object where it represents the title of the art post.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    artist = models.ForeignKey(
    UserProfile, on_delete=models.CASCADE, related_name="art_posts",)
    about = models.TextField()
    art_image = CloudinaryField('art_image', default='art_placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1600), MaxValueValidator(datetime.date.today().year)], default=datetime.date.today().year)
    condition = models.IntegerField(choices=CONDITION, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of artwork post is {self.title}"


class Like(models.Model):
    """
    This is a Like model that represents a like given by a user to a piece of art.

    Attributes:
    user (ForeignKey): Represents the user who liked the art. If the user profile is deleted, all their likes will also be deleted.
    art (ForeignKey): Represents the art that the user liked. If the art post is deleted, all associated likes will also be deleted.

    Meta:
    Ensures every like is unique at a user-art level, i.e, each user can only like each piece of art once.

    Methods:
    __str__(): Returns a readable string representation of the Like object, indicating which user liked which art.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'art')

    def __str__(self):
        return f"{self.user.username} likes {self.art.title}"


class Review(models.Model):
    """
    This is a Review model that represents a review made by a user on a piece of art.

    Attributes:
    art (ForeignKey): Represents the art that the review was made on. On deletion of the art, associated reviews will also be deleted.
    author (ForeignKey): Represents the user who wrote the review. On deletion of the user, all their reviews will also be deleted.
    body (TextField): The text body of the review.
    rating (IntegerField): The rating given by the user to the art. Values should fall between 1 and 5.
    approved (BooleanField): Indicates whether the review is approved or not; default value is False.
    created_on (DateTimeField): The date and time when the review was created, automatically set when the object is first created.

    Meta:
    Orders the reviews by the date and time they were created on.

    Methods:
    __str__(): Returns a readable string representation of the Review object, indicating which review body is by which author.
    """
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="reviewer"
    )
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"
