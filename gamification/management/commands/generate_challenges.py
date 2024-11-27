from django.core.management.base import BaseCommand
from datetime import date
import random
from gamification.models import DailyChallenge, ChallengeTemplate
from users.models import User

class Command(BaseCommand):
    help = 'Generate daily challenges for all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        challenge_templates = ChallengeTemplate.objects.all()

        for user in users:
            if DailyChallenge.objects.filter(user=user, date_assigned=date.today()).exists():
                continue

            if challenge_templates.exists():
                challenge_template = random.choice(challenge_templates)
                DailyChallenge.objects.create(
                    user=user,
                    task=challenge_template.task,
                    date_assigned=date.today()
                )
                self.stdout.write(f"Challenge created for {user.username}: {challenge_template.task}")