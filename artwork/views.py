from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Art

# Create your views here.
class ArtList(generic.ListView):
    queryset = Art.objects.all()
    template_name = "index.html"
    paginate_by = 6


def art_details(request, art_slug):
    art = get_object_or_404(Art, slug=art_slug)
    return render(request, 'art_detail.html', {'art': art})