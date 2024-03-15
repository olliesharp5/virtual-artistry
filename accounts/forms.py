from django import forms
from django.contrib.auth.models import User
from artists.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'display_name', 'location', 'profile_image', 'about']

class UpdateProfileForm(UserProfileForm):
    class Meta(UserProfileForm.Meta):
        fields = ['display_name', 'location', 'profile_image', 'about']