import cloudinary
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from artists.models import UserProfile
from .models import Art, Review, Like
from .forms import ReviewForm, ArtForm
from .filters import ArtFilter

# Create your views here.
class ArtList(generic.ListView):
    """
    Returns a random list of Art objects from :model:`art.Art` (excluding those with status 0), 
    which can be further filtered using `ArtFilter`. 

    **Context**

    ``filter``
    An instance of `ArtFilter` to enable filtering on the queryset.

    **Methods**

    ``get_queryset()``
    Returns a random queryset of Art objects, excluding those with status 0 and applies `ArtFilter`.

    ``get_context_data(**kwargs)``
    Adds `filter` to template context.

    **Template:**

    :template:`index.html`
    """
    model = Art
    template_name = "artwork/index.html"
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(status=0)
        self.filter = ArtFilter(self.request.GET, queryset=queryset)
        return self.filter.qs.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter

         # Generate the URLs for the resized images
        for art in context['object_list']:
            if art.art_image:
                art.resized_image_url = cloudinary.utils.cloudinary_url(art.art_image.public_id, width=500, crop="scale")[0]

        return context


def art_details(request, art_slug):
    """
    Displays the detail view of a specific Art object along with its associated reviews 
    from :model:`art.Review`, and allows users to add new reviews if authenticated.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``art_slug``
    Slug of the Art object.

    **Context**

    ``art``
    Instance of the Art object.
    ``user_has_liked``
    Boolean flag indicating if the current user has liked the art.
    ``review_form``
    A form instance for posting a new review.
    ``reviews``
    List of approved Review objects linked to the Art object.
    ``artist_profile``
    The profile of the artist who created the Art.

    **Template:**

    :template:`art_detail.html`
    """
    art = get_object_or_404(Art, slug=art_slug)
    user_has_liked = Like.objects.filter(user=request.user.userprofile, art=art).exists() if request.user.is_authenticated else False
    artist_profile = art.artist
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.art = art
        review.author = request.user.userprofile  # Set the author to the current user.profile
        review.save()
    reviews = Review.objects.filter(art=art, approved=True)  # Fetch approved reviews
    return render(request, 'artwork/art_detail.html', 
        {'art': art, 'user_has_liked': user_has_liked, 'review_form': form, 'reviews': reviews, 'artist_profile': artist_profile,}
    )


def create_advert(request):
    """
    Handles the creation of a new art advert from the :model:`art.Art`. 

    **Arguments:**

    ``request``
    The HTTP request.

    **POST:**

    Art information is validated and if valid, a new Art instance is created with status set to 0. 
    The user is redirected to the home page.

    **GET:**

    An empty ArtForm is displayed.

    **Template:**

    :template:`create_art.html`
    """
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_advert = form.save(commit=False) # don't save it immediately
            new_advert.status = 0 # set the status to 0
            new_advert.save() # now save it
            messages.success(request, 'Your art advert has been created and is pending review by an admin.')
            return redirect('home')
    else:
        form = ArtForm(user=request.user)
    return render(request, 'artwork/create_art.html', {'form': form})

@login_required
def like_artwork(request, art_slug):
    """
    Handles the request of a user liking or un-liking an Art object from the :model:`art.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``art_slug``
    Slug of the Art object.

    After liking or unliking an artwork, redirects to the details of the Art object. 
    Only authenticated users can access this view.
    """
    artwork = get_object_or_404(Art, slug=art_slug)
    like = Like.objects.filter(user=request.user.userprofile, art=artwork)
    if like.exists():
        like.first().delete()
    else:
        Like.objects.create(user=request.user.userprofile, art=artwork)
    return redirect('art_details', art_slug=artwork.slug)


def review(request):
    """
    Handles the creation of a new Review for an Art object from the :model:`art.Review`.

    **Arguments:**

    ``request``
    The HTTP request.

    **POST:**

    Review information is validated and if valid, a new Review instance is created and saved. 
    The user is redirected to the Art details.

    **GET:**

    An empty ReviewForm is displayed.

    **Template:**

    :template:`art_detail.html`
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been sent for admin approval')
            return redirect('art_details', art_slug=artwork.slug)
    else:
        form = ReviewForm()
    return render(request, 'artwork/art_detail.html', {'form': form})


def review_edit(request, art_slug, review_id):
    """
    Handles the editing of an existing review associated with an Art object from the :model:`art.Review`.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``art_slug``
    Slug of the Art object. 
    ``review_id``
    ID of the Review object.

    After successfully editing a review, redirects to the details of the Art object.
    """
    if request.method == "POST":

        queryset = Review.objects.filter(approved=True)
        product = get_object_or_404(Art, slug=art_slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user.userprofile:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
    
    return HttpResponseRedirect(reverse('art_details', args=[art_slug]))


def review_delete(request, art_slug, review_id):
    """
        Handles the deletion of an existing review associated with an Art object from the :model:`art.Review`.

        **Arguments:**

        ``request``
        The HTTP request. 
        ``art_slug``
        Slug of the Art object. 
        ``review_id``
        ID of the Review object.

        After successfully deleting a review, redirects to the details of the Art object.
        """
    queryset = Review.objects.filter(approved=True)
    product = get_object_or_404(Art, slug=art_slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user.userprofile:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('art_details', args=[art_slug]))


def artwork_edit(request, art_slug):
    """
    Handles the editing of an existing Art object from the :model:`art.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``art_slug``
    Slug of the Art object. 

    After successfully editing an artwork, the artwork's status is set to 0 (draft) and it is saved. The user is then redirected to the 'home' URL.
    """
    if request.method == "POST":
        art = get_object_or_404(Art, slug=art_slug)
        art_form = ArtForm(data=request.POST, instance=art, user=request.user)  # pass the user here

        if art_form.is_valid() and art.artist == request.user.userprofile:
            art = art_form.save(commit=False)
            art.status = 0  # setting status to 0: draft
            art.save()
            messages.add_message(request, messages.SUCCESS, 'Artwork awaiting admin review!')
            return redirect('home')  # redirect to 'home' URL
        else:
            messages.add_message(request, messages.ERROR, 'Error updating artwork!')
    
    return HttpResponseRedirect(reverse('art_details', args=[art_slug]))


def artwork_delete(request, art_slug):
    """
    Handles the deletion of an existing Art object from the :model:`art.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 
    ``art_slug``
    Slug of the Art object. 

    After successfully deleting an artwork, the user is redirected to the 'home' URL. If the authenticated user is not the creator of the artwork, it redirects to the artwork details page.
    """
    art = get_object_or_404(Art, slug=art_slug)

    if art.artist == request.user.userprofile:
        art.delete()
        messages.add_message(request, messages.SUCCESS, 'Artwork deleted!')
        return redirect('home')  # redirect to 'home' URL
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own artwork!')
        return HttpResponseRedirect(reverse('art_details', args=[art_slug]))  # redirect to art details page if the user is not the artist

