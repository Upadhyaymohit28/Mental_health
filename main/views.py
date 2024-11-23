from django.shortcuts import render, redirect
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

def home(request):
    return render(request, 'main/home.html')


def crisis_support(request):
    return render(request, 'main/crisis_support.html')


def resources(request):
    return render(request, 'main/resources.html')


def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')



# Set your OpenAI API key
openai.api_key = "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"

import openai
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Configure logging
logger = logging.getLogger(__name__)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"  # Replace with your actual API key

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            logger.debug(f"Received data: {data}")

            user_message = data.get('message', '')
            if not user_message:
                logger.error("Empty user message received.")
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            # Generate response using OpenAI's Completion API
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the correct engine
                prompt=f"User: {user_message}\nAI:",
                max_tokens=150,
                temperature=0.7,
            )

            # Extract the AI's message
            ai_message = response['choices'][0]['text'].strip()
            logger.debug(f"AI Response: {ai_message}")

            return JsonResponse({"message": ai_message})

        except openai.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return JsonResponse({"error": f"OpenAI API error: {str(e)}"}, status=500)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"error": f"Something went wrong: {str(e)}"}, status=500)
    else:
        logger.error("Invalid request method.")
        return JsonResponse({"error": "Invalid request method"}, status=400)
