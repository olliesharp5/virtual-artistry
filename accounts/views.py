from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from artists.models import UserProfile

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
    context = {'userprofile': user_profile}
    return render(request, 'accounts/profile.html', context)