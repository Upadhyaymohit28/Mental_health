from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_content, name='list_content'),
]