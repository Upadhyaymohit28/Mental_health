from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Badge, Streak, DailyChallenge


@login_required
def badges(request):
    user_badges = request.user.badges.all()
    return render(request, 'gamification/badges.html', {'badges': user_badges})


@login_required
def streaks(request):
    user_streak = request.user.streaks.first()  # Assuming one streak per user
    return render(request, 'gamification/streaks.html', {'streak': user_streak})


@login_required
def daily_challenge(request):
    today_challenge = DailyChallenge.objects.filter(user=request.user, date_assigned=date.today()).first()

    if request.method == 'POST' and 'complete_challenge' in request.POST:
        if today_challenge:
            today_challenge.is_completed = True
            today_challenge.save()

    return render(request, 'gamification/daily_challenge.html', {'challenge': today_challenge})
