from .main_views import (
    signup,
    login_user,
    logout_user,
    dashboard,
    profile,
    update_profile,
    mood_tracking,  
    video_recommendations,  
    consultation,
    gamification,
    recommendation_detail,   
)
from .notifications import (
    notifications_view,
    mark_all_read,
    mark_as_read,
)
from django.shortcuts import render, get_object_or_404
from content.models import EducationalContent


__all__ = [
    "signup",
    "login_user",
    "logout_user",
    "dashboard",
    "profile",
    "update_profile",
    "notifications_view",
    "mark_all_read",
    "mark_as_read",
    "mood_tracking",  
    "video_recommendations",  
    "consultation",  
    "gamification",
    "recommendation_detail",
]
