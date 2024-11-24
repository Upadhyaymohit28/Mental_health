from django.urls import path
from .views import *  # 导入 __init__.py 中定义的所有函数

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
]
