from django.shortcuts import render
from django.http import JsonResponse
import requests

def chatbot(request):
    return render(request, 'chatbot.html')

def get_chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        # Replace 'YOUR_API_KEY' with your actual ChatGPT API key
        api_key = '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'
        chatgpt_url = 'https://api.openai.com/v1/chat/completions'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': user_message}
            ]
        }

        response = requests.post(chatgpt_url, headers=headers, json=data)
        response_data = response.json()
        print("Response from ChatGPT API:", response_data)

        if 'choices' in response_data and response_data['choices']:
            chatbot_response = response_data['choices'][0]['message']['content']
            return JsonResponse({'chatbot_response': chatbot_response})
        else:
            return JsonResponse({'error': 'Invalid response format or empty response from ChatGPT API'})

    else:
        return JsonResponse({'error': 'Invalid request method'})


