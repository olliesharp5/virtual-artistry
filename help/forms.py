from django import forms
from .models import HelpRequest

class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ('name', 'email', 'message')