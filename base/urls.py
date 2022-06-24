from django.urls import path

from base import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
]
