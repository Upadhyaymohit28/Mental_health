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

# Session tracker for doctor chats
conversation_start_time = {}

# Doctor-specific configurations
DOCTOR_PROFILES = {
    1: "Dr. Jane Smith, a psychiatrist specializing in anxiety and depression.",
    2: "Dr. John Doe, a psychiatrist focused on cognitive behavioral therapy.",
    3: "Dr. Emily White, a psychiatrist with expertise in mindfulness and stress management.",
}
@csrf_exempt
def chatbot_response(request):
    global conversation_start_time
    logger.info("Entering chatbot_response function")

    if request.method == 'POST':
        try:
            # Parse request data
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            doctor_id = int(data.get('doctor_id')) if data.get('doctor_id') else None

            if not user_message:
                logger.error("Message is empty")
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            if doctor_id:
                # Validate doctor ID
                if doctor_id not in DOCTOR_PROFILES:
                    return JsonResponse({"error": "Invalid doctor ID provided."}, status=400)

                # Handle doctor-specific chat logic
                if doctor_id not in conversation_start_time:
                    conversation_start_time[doctor_id] = datetime.now()

                if datetime.now() - conversation_start_time[doctor_id] > timedelta(minutes=15):
                    conversation_start_time.pop(doctor_id)  # Clear expired session
                    return JsonResponse({
                        "message": "Your session with the doctor has ended. Please book an appointment for further assistance."
                    })

                system_message = (
                    f"You are {DOCTOR_PROFILES[doctor_id]}. "
                    "Converse as the doctor would, and discuss only topics related to mental health. "
                    "Do not provide medical diagnoses or unrelated advice."
                )
            else:
                # General chatbot logic
                system_message = (
                    "You are a professional and empathetic assistant for a mental health platform. "
                    "Provide support on mindfulness, stress management, and emotional well-being. "
                    "Suggest available doctors for specific queries and answer questions about subscriptions and benefits of the app."
                )

                # Handle general queries
                keywords_subscription = ["subscription", "pricing", "benefits", "features"]
                if any(keyword in user_message.lower() for keyword in keywords_subscription):
                    return JsonResponse({
                        "message": (
                            "Our app offers personalized mental health support, mood tracking, mindfulness exercises, "
                            "and access to licensed professionals. You can explore our subscription plans on the 'Pricing' page."
                        )
                    })

                if "doctor" in user_message.lower():
                    doctor_options = ", ".join([f"{doc_id}: {doc}" for doc_id, doc in DOCTOR_PROFILES.items()])
                    return JsonResponse({
                        "message": f"We have the following doctors available:\n{doctor_options}. "
                                   "Please provide the doctor number to start a conversation."
                    })

            # Call OpenAI API for the AI's response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=200,
                temperature=0.7,
            )

            ai_message = response['choices'][0]['message']['content'].strip()
            logger.debug(f"AI Response: {ai_message}")
            return JsonResponse({"message": ai_message})

        except openai.OpenAIError as e:
            logger.error(f"OpenAI API error: {e}")
            return JsonResponse({"error": f"OpenAI API error: {str(e)}"}, status=500)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Decode Error: {e}")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    logger.error("Invalid request method")
    return JsonResponse({"error": "Invalid request method"}, status=400)