from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Badge, Streak, DailyChallenge
from .models import ChallengeTemplate, Badge

def gamification_home(request):
    """
    Gamification 首页视图函数
    """
    # 从模型中获取每日挑战和徽章信息
    daily_challenges = ChallengeTemplate.objects.filter(category='Daily')[:5]  # 只取前5个每日挑战
    user_badges = Badge.objects.filter(user=request.user)  # 获取当前用户的徽章

    # 渲染模板并传递数据
    return render(request, 'gamification/gamification_home.html', {
        'daily_challenges': daily_challenges,
        'user_badges': user_badges,
    })

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
