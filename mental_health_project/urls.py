from django.contrib import admin
from django.urls import path, include

from chatbot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('moodtracking/', include('moodtracking.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('gamification/', include('gamification.urls')),
    path('content/', include('content.urls')),
    path('support/', include('support.urls')),
]
