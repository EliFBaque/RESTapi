from django.shortcuts import render

from base.forms import UserForm

from profiles_api.models import UserProfile

# Create your views here.

def home(request):
    """trying things first"""
    """User creation on form is correct"""
    '''form = UserForm()
    context = {'form' : form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise ValueError('Form is not valid')'''
    
    
    return render(request, 'base/home.html')#, context)

def contact(request):
    """contact page"""
    
    return render(request, 'containers/contact.html')


def login(request):
    """login page"""
    return render(request, 'registration/login.html')

def signin(request):
    """signin page"""
    return render(request, 'registration/signin.html')


