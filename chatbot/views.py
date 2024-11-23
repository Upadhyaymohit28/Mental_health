


import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai

# Configure logging
logger = logging.getLogger(__name__)

# Set your OpenAI API key

openai.api_key = "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"


@csrf_exempt
def chatbot_response(request):
    logger.debug("Entering chatbot_response function")
    if request.method == 'POST':
        try:
            # Parse request data
            logger.debug("Reading request body")
            data = json.loads(request.body)
            logger.debug(f"Received data: {data}")

            # Validate user message
            user_message = data.get('message', '')
            if not user_message:
                logger.error("Message is empty")
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            # Call OpenAI API
            logger.debug(f"Calling OpenAI API with message: {user_message}")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"User: {user_message}\nAI:",
                max_tokens=150,
                temperature=0.7,
            )

            # Extract AI response
            ai_message = response['choices'][0]['text'].strip()
            logger.debug(f"AI Response: {ai_message}")
            return JsonResponse({"message": ai_message})

        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return JsonResponse({"error": f"OpenAI API error: {str(e)}"}, status=500)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    logger.error("Invalid request method")
    return JsonResponse({"error": "Invalid request method"}, status=400)
