from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ArtistProfile

# Create your views here.
class ArtistList(generic.ListView):
    queryset = ArtistProfile.objects.all()
    template_name = "artists.html"
    paginate_by = 6


def artist_profile(request, artist_id):
    artist = get_object_or_404(ArtistProfile, pk=artist_id)
    return render(request, 'artist_profile.html', {'artist': artist})