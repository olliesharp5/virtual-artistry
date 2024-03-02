from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Art, Review, Like
from artists.models import ArtistProfile
from .forms import ReviewForm
from .filters import ArtFilter

# Create your views here.
class ArtList(generic.ListView):
    model = Art
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = ArtFilter(self.request.GET, queryset=queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


def art_details(request, art_slug):
    art = get_object_or_404(Art, slug=art_slug)
    user_has_liked = Like.objects.filter(user=request.user, art=art).exists() if request.user.is_authenticated else False
    artist_profile = art.artist
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.art = art
        review.author = request.user  # Set the author to the current user
        review.save()
    reviews = Review.objects.filter(art=art, approved=True)  # Fetch approved reviews
    return render(request, 'art_detail.html', {'art': art, 'user_has_liked': user_has_liked, 'review_form': form, 'reviews': reviews, 'artist_profile': artist_profile,})

@login_required
def like_artwork(request, art_slug):
    artwork = get_object_or_404(Art, slug=art_slug)
    like = Like.objects.filter(user=request.user, art=artwork)
    if like.exists():
        like.first().delete()
    else:
        Like.objects.create(user=request.user, art=artwork)
    return redirect('art_details', art_slug=artwork.slug)


def review_edit(request, art_slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Review.objects.filter(approved=True)
        product = get_object_or_404(Art, slug=art_slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
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
    view to delete reviews
    """
    queryset = Review.objects.filter(approved=True)
    product = get_object_or_404(Art, slug=art_slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('art_details', args=[art_slug]))