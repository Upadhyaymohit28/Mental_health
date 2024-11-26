from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('doctor-chatbots/', TemplateView.as_view(template_name="main/doctor_chatbots.html"), name='doctor_chatbots'),
]
