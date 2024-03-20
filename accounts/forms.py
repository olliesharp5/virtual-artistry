from django import forms
from django.contrib.auth.models import User
from artists.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'display_name', 'location', 'profile_image', 'about']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = [(tag[0], tag[1]) for tag in UserProfile.USER_ROLES if tag[0] in ['RU', 'AR']]

class UpdateProfileForm(UserProfileForm):
    class Meta(UserProfileForm.Meta):
        fields = ['display_name', 'location', 'profile_image', 'about']