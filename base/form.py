from django import forms
from profiles_api.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = UserProfile
        fields = ('email', 'name', 'password')