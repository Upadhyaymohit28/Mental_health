# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_mood/', views.add_mood, name='add_mood'),
    path('mood_history/', views.mood_history, name='mood_history'),

    path('crisis_support/', views.crisis_support, name='crisis_support'),
    path('resources/', views.resources, name='resources'),
]
