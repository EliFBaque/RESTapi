from multiprocessing.sharedctypes import Value
from django.shortcuts import redirect, render

#from .forms import UserForm
from profiles_api.models import UserProfile
from profiles_api.serializers import UserProfileSerializer 
from profiles_api.views import UserProfileViewSet, UserList
from profiles_api import views

from .form import UserForm




# Create your views here.

def home(request):
    """trying things first"""
    users = UserProfile.objects.all()
    context = {'users': users}
    return render(request, 'base/home.html', context)

def contact(request):
    """contact page"""
    return render(request, 'base/containers/contact.html')

def loginPage(request):
    """login page"""
    return render(request, 'base/registration/login.html')

def SignInPage(request):
    """User creation on form is correct"""    
    user = UserProfileViewSet.serializer_class()
    context = {'user' : user}
    
    if request.method == 'POST':
        user = UserProfileViewSet.serializer_class(data=request.POST)
        print(UserProfileViewSet.serializer_class(data=request.POST))
        if user.is_valid():
            user.save()
        else:
            raise ValueError('Form is not valid')
        # Sigue siendo lo mismo necesito hacer algun cambio
    return render(request, 'base/registration/signin.html', context)


