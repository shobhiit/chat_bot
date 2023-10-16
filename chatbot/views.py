from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Chat_messages
import openai
from chatbot_project.settings import api_key
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chatbot')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chatbot')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def chatbot(request):
       
    chat_history = Chat_messages.objects.filter(user=request.user).order_by('created_at')

    context = {
        'chat_history': chat_history,
    }

    return render(request, 'chatbot.html', context)

def get_chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        openai.api_key = api_key 

        # Define the conversation history
        conversation_history = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': user_message}
        ]
        # Use the OpenAI API to generate a response
        response_data = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        if 'choices' in response_data and response_data['choices']:
            chatbot_response = response_data['choices'][0]['message']['content']
            # Save the conversation to the database
            try:
                Chat_messages.objects.create(
                    user=request.user,
                    user_text=user_message,
                    bot_text=chatbot_response
                )
            except Exception as e:
                print(f"Error creating Chat_messages object: {e}")

            return JsonResponse({'chatbot_response': chatbot_response})
        else:
            return JsonResponse({'error': 'Invalid response format or empty response from ChatGPT API'})

    else:
        return JsonResponse({'error': 'Invalid request method'})