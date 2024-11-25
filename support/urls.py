from django.urls import path
from . import views

urlpatterns = [
    path('resources/', views.support_resources, name='support_resources'),
]