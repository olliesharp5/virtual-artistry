from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, UserProfileForm, UpdateProfileForm
from artwork.forms import ArtForm
from artists.models import UserProfile
from artwork.models import Art


# Create your views here.

def register(request):
    """
    Handles the creation of a new user and their profile in :model:`accounts.User` and :model:`accounts.UserProfile`. 

    **Arguments:**

    ``request``
    The HTTP request. 

    **POST:**

    User information is validated and if valid, a new User is created along with their profile. 
    After creation, the user is redirected to the home page.

    **GET:**

    An empty registration form for User and UserProfile is displayed.

    **Template:**

    :template:`accounts/register.html`
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})


def profile(request):
    """
    Displays the profile of the currently logged in user from :model:`accounts.UserProfile`.

    **Arguments:**

    ``request``
    The HTTP request. 

    **Context**

    ``userprofile``
    Instance of the currently logged in user's profile.

    **Template:**

    :template:`accounts/profile.html`
    """
    user_profile = UserProfile.objects.get(user=request.user)
    user = request.user
    artistprofile = UserProfile.objects.get(user=user)
    pending_artworks = Art.objects.filter(artist=artistprofile).exclude(status=1)
    context = {
        'userprofile': user_profile,
        'draft_object_list': pending_artworks
    }
    return render(request, 'accounts/profile.html', context)


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def delete_user_profile(request):
    user = request.user
    user_profile = user.userprofile
    user_profile.delete()
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Profile deleted!')
    logout(request)
    return redirect('home')  # redirect to 'home' URL


def draft_artwork_edit(request, art_slug):
    if request.method == "POST":
        art = get_object_or_404(Art, slug=art_slug)
        art_form = ArtForm(data=request.POST, instance=art, user=request.user)

        if art_form.is_valid():
            art = art_form.save(commit=False)
            art.status = 0  # setting status to 0: draft
            art.save()
            messages.add_message(request, messages.SUCCESS, 'Artwork awaiting admin review!')
            return redirect('/accounts/signup/profile/')  # redirect to 'profile' URL
        else:
            print(art_form.errors)
            messages.add_message(request, messages.ERROR, 'Error updating artwork!')
    
    return HttpResponseRedirect(reverse('art_details', args=[art_slug]))


def draft_artwork_delete(request, art_slug):
    art = get_object_or_404(Art, slug=art_slug)
    art.delete()
    messages.add_message(request, messages.SUCCESS, 'Draft deleted!')
    return redirect('profile')  # redirect to 'profile' URL