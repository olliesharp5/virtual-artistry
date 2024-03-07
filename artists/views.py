from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django_filters.views import FilterView
from .models import UserProfile
from artwork.models import Art
from .filters import UserProfileFilter

# Create your views here.
class ArtistList(FilterView):
    filterset_class = UserProfileFilter
    template_name = "artists.html"
    paginate_by = 6

    def get_queryset(self):
        return UserProfile.objects.filter(role='AR')


def artist_profile(request, username):
    user = get_object_or_404(User, username=username)
    artistprofile = UserProfile.objects.get(user=user)
    artworks = Art.objects.filter(artist=artistprofile)
    return render(request, 'artist_profile.html', {'artistprofile': artistprofile, 'object_list': artworks})
