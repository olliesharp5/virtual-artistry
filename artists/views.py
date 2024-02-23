from django.shortcuts import render
from django.views import generic
from .models import ArtistProfile

# Create your views here.
class ArtistList(generic.ListView):
    queryset = ArtistProfile.objects.all()
    template_name = "artists.html"
    paginate_by = 6