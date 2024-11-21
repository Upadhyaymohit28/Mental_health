from django.urls import path
from . import views

urlpatterns = [
    path('mood_history/', views.mood_history, name='mood_history'),
]
