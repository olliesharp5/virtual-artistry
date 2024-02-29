from django.shortcuts import render, get_object_or_404
from django.views import generic
from django_filters.views import FilterView
from .models import ArtistProfile
from artwork.models import Art
from .filters import ArtistProfileFilter

# Create your views here.
class ArtistList(FilterView):
    filterset_class = ArtistProfileFilter
    template_name = "artists.html"
    paginate_by = 6

    def get_queryset(self):
        return ArtistProfile.objects.all()


def artist_profile(request, artist_slug):
    artistprofile = get_object_or_404(ArtistProfile, slug=artist_slug)
    artworks = Art.objects.filter(artist=artistprofile)
    return render(request, 'artist_profile.html', {'artistprofile': artistprofile, 'object_list': artworks})