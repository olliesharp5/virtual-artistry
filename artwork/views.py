from django.shortcuts import render
from django.views import generic
from .models import Art

# Create your views here.
class ArtList(generic.ListView):
    queryset = Art.objects.all()
    template_name = "artwork_list.html"