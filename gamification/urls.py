from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamification_home, name='gamification_home'),
    path('badges/', views.badges, name='badges'),
    path('streaks/', views.streaks, name='streaks'),
    path('daily-challenge/', views.daily_challenge, name='daily_challenge'),
]
