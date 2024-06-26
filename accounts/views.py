from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from artwork.forms import ArtForm
from artists.models import UserProfile
from artwork.models import Art
from .forms import UserForm, UserProfileForm, UpdateProfileForm, UpdateUserForm


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
            user = user_form.save(commit=False)  # Don't save the User instance yet
            user.set_password(user_form.cleaned_data['password'])  # Set the password
            user.save()  # Now save the User instance
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # Log in the user
            messages.add_message(request, messages.SUCCESS, 'Congratulations, you have successfully registered!')
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
    """
    Updates the profile of the currently logged in user from :model:`accounts.UserProfile`.

    **Arguments:**

    ``request``
    The HTTP request. 

    **Context**

    ``user_form``
    Form instance for updating user details.

    ``profile_form``
    Form instance for updating profile details.

    **Template:**

    :template:`accounts/update_profile.html`
    """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def delete_user_profile(request):
    """
    Deletes the profile of the currently logged in user from :model:`accounts.UserProfile`.

    **Arguments:**

    ``request``
    The HTTP request. 

    **Context**

    ``user``
    Instance of the currently logged in user.

    **Template:**

    :template:`accounts/home.html`
    """
    user = request.user
    user_profile = user.userprofile
    user_profile.delete()
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Profile deleted!')
    logout(request)
    return redirect('home')  # redirect to 'home' URL


def draft_artwork_edit(request, art_slug):
    """
    Edits the draft artwork of the currently logged in user from :model:`accounts.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 

    ``art_slug``
    The slug of the artwork to be edited.

    **Context**

    ``art_form``
    Form instance for updating artwork details.

    **Template:**

    :template:`accounts/art_details.html`
    """
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
    """
    Deletes the draft artwork of the currently logged in user from :model:`accounts.Art`.

    **Arguments:**

    ``request``
    The HTTP request. 

    ``art_slug``
    The slug of the artwork to be deleted.

    **Context**

    ``art``
    Instance of the artwork to be deleted.

    **Template:**

    :template:`accounts/profile.html`
    """
    art = get_object_or_404(Art, slug=art_slug)
    art.delete()
    messages.add_message(request, messages.SUCCESS, 'Draft deleted!')
    return redirect('profile')  # redirect to 'profile' URL