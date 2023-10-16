from django.urls import path
from .views import chatbot, get_chatbot_response, register, user_login,user_logout

urlpatterns = [
    
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('chatbot/', chatbot, name='chatbot'),
    path('get_chatbot_response/', get_chatbot_response, name='get_chatbot_response'),
]
