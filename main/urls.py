from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crisis_support/', views.crisis_support, name='crisis_support'),
    path('resources/', views.resources, name='resources'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    
]
