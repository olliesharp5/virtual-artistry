from django import forms
from django.utils.text import slugify
from .models import Review, Art
from artists.models import UserProfile

# form for creating art adverts 
class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'about', 'art_image', 'price', 'year', 'condition']
        labels = {
            'art_image': 'Image',
         }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ArtForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ArtForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.status = 0
        instance.artist = UserProfile.objects.get(user=self.user)

        if commit:
            instance.save()
        return instance


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'rating')
