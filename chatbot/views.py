from django.shortcuts import render
from django.http import JsonResponse

import openai

openai_api_key= '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'
openai.api_key= openai_api_key


def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )

    answer = response['choices'][0]['text']
    return answer




# Create your views here.

def chatbot(request):
    if request.method == 'POST':
        message= request.POST.get('message')
        
        response= ask_openai(message)
        print(response)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
