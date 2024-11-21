from django.urls import path
from . import views

urlpatterns = [
    path('badges/', views.badges, name='badges'),
    path('streaks/', views.streaks, name='streaks'),
    path('daily-challenge/', views.daily_challenge, name='daily_challenge'),
]
