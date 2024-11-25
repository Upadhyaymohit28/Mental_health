
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from datetime import datetime, timedelta

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
            data = json.loads(request.body)
            logger.debug(f"Received data: {data}")

            # Validate user message
            user_message = data.get('message', '').strip().strip()
            if not user_message:
                logger.error("Message is empty")
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            # Default system message for the AI
            system_message = (
                "You are a professional and empathetic assistant for a mental health platform. "
                "You provide support on mindfulness, stress management, and emotional well-being. "
                "Additionally, always remind users that they can book an appointment with licensed mental health professionals on this platform."
            )

            # Default system message for the AI
            system_message = (
                "You are a professional and empathetic assistant for a mental health platform. "
                "You provide support on mindfulness, stress management, and emotional well-being. "
                "Additionally, always remind users that they can book an appointment with licensed mental health professionals on this platform."
            )

            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=200,
                temperature=0.7,
            )

            # Extract AI response
            ai_message = response['choices'][0]['message']['content'].strip()
            ai_message = response['choices'][0]['message']['content'].strip()
            logger.debug(f"AI Response: {ai_message}")

            # Logic for appointment suggestions
            booking_link = "https://www.mentalhealthapp.com/book-appointment"
            keywords = ["doctor", "appointment", "meet doctor", "help from professional"]

            if any(keyword in user_message.lower() for keyword in keywords):
                ai_message = (
                    "We have licensed mental health professionals available to support you. "
                    f"You can book an appointment with one of our doctors here: [Book an Appointment]({booking_link}). "
                    "If you'd like, I can guide you on how to proceed further."
                )


            # Logic for appointment suggestions
            booking_link = "https://www.mentalhealthapp.com/book-appointment"
            keywords = ["doctor", "appointment", "meet doctor", "help from professional"]

            if any(keyword in user_message.lower() for keyword in keywords):
                ai_message = (
                    "We have licensed mental health professionals available to support you. "
                    f"You can book an appointment with one of our doctors here: [Book an Appointment]({booking_link}). "
                    "If you'd like, I can guide you on how to proceed further."
                )

            return JsonResponse({"message": ai_message})

        except openai.error.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return JsonResponse({"error": f"OpenAI API error: {str(e)}"}, status=500)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Decode Error: {e}")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Decode Error: {e}")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    logger.error("Invalid request method")
    return JsonResponse({"error": "Invalid request method"}, status=400)