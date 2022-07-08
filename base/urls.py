from django.urls import path

from base import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('signin/', views.SignInPage, name='signin'),
]
