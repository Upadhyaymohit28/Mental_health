from .main_views import (
    signup,
    login_user,
    logout_user,
    dashboard,
    profile,
    update_profile,
<<<<<<< HEAD
    mood_tracking,  
    video_recommendations,  
    consultation,
    recommendation_detail,   
=======
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
)
from .notifications import (
    notifications_view,
    mark_all_read,
    mark_as_read,
)
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from content.models import EducationalContent


=======

# 导出所有需要的视图函数
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
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
<<<<<<< HEAD
    "mood_tracking",  
    "video_recommendations",  
    "consultation",  
    "recommendation_detail",
=======
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
]
