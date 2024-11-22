from django.core.management.base import BaseCommand
from gamification.models import ChallengeTemplate


class Command(BaseCommand):
    help = 'Populate challenge templates'

    def handle(self, *args, **kwargs):
        challenges = [
            # Mental well-being
            {"task": "Take 10 deep breaths and focus on your breathing.", "difficulty": "Easy"},
            {"task": "Write down three things you're grateful for today.", "difficulty": "Easy"},
            {"task": "Write a short journal entry about how you feel today.", "difficulty": "Medium"},
            {"task": "Spend 5 minutes meditating or listening to calming music.", "difficulty": "Easy"},
            {"task": "Read a chapter of a self-help or motivational book.", "difficulty": "Medium"},
            {"task": "Spend 15 minutes practicing mindfulness meditation.", "difficulty": "Hard"},
            {"task": "Create a simple plan for tomorrow's tasks.", "difficulty": "Easy"},

            # Physical well-being
            {"task": "Go for a 15-minute walk and observe your surroundings.", "difficulty": "Medium"},
            {"task": "Drink 8 glasses of water today.", "difficulty": "Easy"},
            {"task": "Stretch for 10 minutes to relieve tension.", "difficulty": "Easy"},
            {"task": "Do 20 minutes of light exercise (e.g., yoga or walking).", "difficulty": "Medium"},
            {"task": "Prepare a healthy meal with fresh ingredients.", "difficulty": "Medium"},
            {"task": "Limit screen time to 1 hour in the evening.", "difficulty": "Hard"},

            # Social well-being
            {"task": "Compliment someone genuinely today.", "difficulty": "Medium"},
            {"task": "Call a friend or family member for a 10-minute chat.", "difficulty": "Medium"},
            {"task": "Write a thank-you note or message to someone you appreciate.", "difficulty": "Medium"},
            {"task": "Join a local group or online community for a shared interest.", "difficulty": "Hard"},
            {"task": "Offer help to someone in need (e.g., carry groceries, hold a door open).", "difficulty": "Easy"},
            {"task": "Have a face-to-face conversation with someone without distractions.", "difficulty": "Medium"},

            # Miscellaneous
            {"task": "Try something new today, like a recipe, hobby, or activity.", "difficulty": "Medium"},
            {"task": "Declutter one small area of your home (e.g., a drawer or desk).", "difficulty": "Medium"},
            {"task": "Watch an inspiring video or listen to a motivational podcast.", "difficulty": "Easy"},
            {"task": "Spend 30 minutes on a creative activity (e.g., drawing, writing).", "difficulty": "Medium"},
            {"task": "Avoid social media for the entire day.", "difficulty": "Hard"},
        ]

        for challenge in challenges:
            ChallengeTemplate.objects.get_or_create(task=challenge['task'], difficulty=challenge['difficulty'])

        self.stdout.write(self.style.SUCCESS(f"{len(challenges)} challenge templates populated successfully!"))