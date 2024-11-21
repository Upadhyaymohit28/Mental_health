from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_mood/', views.add_mood, name='add_mood'),
    path('crisis_support/', views.crisis_support, name='crisis_support'),
    path('resources/', views.resources, name='resources'),
]
