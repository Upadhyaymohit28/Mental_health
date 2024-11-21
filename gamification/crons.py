from django_cron import CronJobBase, Schedule
from datetime import date
import random
from .models import DailyChallenge, ChallengeTemplate
from users.models import User


class GenerateDailyChallengesCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Once a day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'gamification.generate_daily_challenges'

    def do(self):
        users = User.objects.all()
        challenge_templates = ChallengeTemplate.objects.all()

        for user in users:
            if not DailyChallenge.objects.filter(user=user, date_assigned=date.today()).exists():
                challenge_template = random.choice(challenge_templates)
                DailyChallenge.objects.create(
                    user=user,
                    task=challenge_template.task,
                    date_assigned=date.today()
                )
