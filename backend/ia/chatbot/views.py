import os
from dotenv import load_dotenv
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

# Carregar as variáveis de ambiente
load_dotenv()

# Configurar a chave da API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def index(request):
    return render(request, 'chatbot/index.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            # Carregar a mensagem do usuário
            data = json.loads(request.body)
            user_message = data.get('message', '')

            if not user_message:
                return JsonResponse({"error": "A mensagem não pode estar vazia."}, status=400)

            # Fazer a solicitação à API OpenAI utilizando a nova estrutura
            response = openai.completions.create(
                model="gpt-3.5-turbo",  # Modelo atual
                prompt=f"Você é um assistente para ajudar nos estudos. Responda de forma clara e útil:\n\nUsuário: {user_message}\nChatbot:",
                max_tokens=150,
                temperature=0.7
            )

            # Extrair a resposta
            chatbot_reply = response['choices'][0]['text'].strip()

            return JsonResponse({"response": chatbot_reply})
        
        except openai.OpenAIError as e:
            # Captura de erro da OpenAI
            return JsonResponse({"error": f"Erro da API OpenAI: {str(e)}"}, status=500)
        except Exception as e:
            # Erro genérico
            return JsonResponse({"error": f"Erro desconhecido: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método não permitido."}, status=405)
