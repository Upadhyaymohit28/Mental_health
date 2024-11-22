from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_content, name='list_content'),
    path('<int:content_id>/', views.content_detail, name='content_detail'),
]