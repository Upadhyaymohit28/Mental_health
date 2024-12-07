from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Badge, Streak, DailyChallenge
from .models import ChallengeTemplate, Badge

@login_required
def gamification_home(request):
    """
    Gamification home page view function
    """
    # Retrieve daily challenge and badge information from the models
    today_challenge = DailyChallenge.objects.filter(user=request.user, date_assigned=date.today()).first()
    user_badges = Badge.objects.filter(user=request.user)

    # Render the template and pass the data
    return render(request, 'gamification/gamification_home.html', {
        'challenge': today_challenge,
        'user_badges': user_badges,
    })

@login_required
def badges(request):
    # Retrieve all badges for the logged-in user
    user_badges = request.user.badges.all()
    print(f"{user_badges}")
    return render(request, 'gamification/badges.html', {'badges': user_badges})

@login_required
def streaks(request):
    # Retrieve the user's streak (assuming one streak per user)
    user_streak = request.user.streaks.first()
    return render(request, 'gamification/streaks.html', {'streak': user_streak})

@login_required
def daily_challenge(request):
    # Retrieve today's daily challenge for the logged-in user
    today_challenge = DailyChallenge.objects.filter(user=request.user, date_assigned=date.today()).first()

    if request.method == 'POST' and 'complete_challenge' in request.POST:
        # Mark the challenge as completed if it exists
        if today_challenge:
            today_challenge.is_completed = True
            today_challenge.save()

    return render(request, 'gamification/daily_challenge.html', {'challenge': today_challenge})
