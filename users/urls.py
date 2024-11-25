from django.urls import path
<<<<<<< HEAD
from .views import *  
=======
from .views import *  # 导入 __init__.py 中定义的所有函数
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3

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
<<<<<<< HEAD
    path('mood-tracking/', mood_tracking, name='mood_tracking'),
    path('videos/', video_recommendations, name='video_recommendations'),
    path('videos/<int:content_id>/', recommendation_detail, name='recommendation_detail'), 
    path('consultation/', consultation, name='ai_consultation'),
=======
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
]
