from django.urls import path, include
from .views import *  
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('notifications/', notifications_view, name='notifications'),
    path('notifications/mark_all_read/', mark_all_read, name='mark_all_read'),
    path('notifications/mark_as_read/', mark_as_read, name='mark_as_read'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('mood-tracking/', mood_tracking, name='mood_tracking'),
    path('videos/', video_recommendations, name='video_recommendations'),
    path('consultation/', consultation, name='ai_consultation'),
    path('gamification/', gamification, name='gamification'),
]
