from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django_filters.views import FilterView
from artwork.models import Art
from .models import UserProfile
from .filters import UserProfileFilter

# Create your views here.
class ArtistList(FilterView):
    """
    Returns a paginated list of UserProfile instances with 'AR' role (artists) from 
    :model:`accounts.UserProfile`, which can be further filtered using `UserProfileFilter`. 

    **Context**

    ``filter``
    An instance of `UserProfileFilter` to enable filtering on the queryset.

    ``paginate_by``
    Number of artist profiles per page.

    **Methods**

    ``get_queryset()``
    Return a queryset of UserProfile objects with role 'AR'.

    **Template:**

    :template:`artists.html`
    """
    filterset_class = UserProfileFilter
    template_name = "artists/artists.html"
    paginate_by = 6

    def get_queryset(self):
        return UserProfile.objects.filter(role='AR')


def artist_profile(request, username):
    """
    Displays the profile of a specific artist identified by username from :model:`accounts.UserProfile`, 
    along with a list of their artworks (excluding those with status 0) from :model:`art.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``username``
    Username of the artist user.

    **Context**

    ``artistprofile``
    Instance of the artist's user profile.
    ``object_list``
    List of Art objects linked to the artist, excluding those with status 0.

    **Template:**

    :template:`artist_profile.html`
    """
    user = get_object_or_404(User, username=username)
    artistprofile = UserProfile.objects.get(user=user)
    artworks = Art.objects.filter(artist=artistprofile).exclude(status=0)
    return render(request, 'artists/artist_profile.html', {'artistprofile': artistprofile, 'object_list': artworks})
