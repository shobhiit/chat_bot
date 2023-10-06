from django.urls import path
from .views import chatbot, get_chatbot_response

urlpatterns = [
    path('', chatbot, name='chatbot'),
    path('get_chatbot_response/', get_chatbot_response, name='get_chatbot_response'),
]
