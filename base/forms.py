from django import forms

from profiles_api import models


class UserForm(forms.ModelForm):
    """Form to create a new user."""
    class Meta:
        model = models.UserProfile
        fields = ['email', 'name']
        
    