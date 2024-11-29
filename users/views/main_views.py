# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ..forms import UserProfileForm
from ..models import UserProfile, Notification
from moodtracking.models import MoodLog
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from content.models import EducationalContent
import random
from content.models import EducationalContent
from moodtracking.forms import MoodLogForm
from django.shortcuts import redirect
from datetime import date
from gamification.models import ChallengeTemplate, Badge, DailyChallenge


def signup(request):
    form = UserCreationForm(request.POST or None)  # 初始化表单，无需重复判断
    error_messages = []

    if request.method == 'POST':
        print("POST request received")
        if form.is_valid():
            print("Form is valid")
            # 保存新用户
            user = form.save()
            # 登录新用户
            login(request, user)

            # 创建通知
            Notification.objects.create(
                user=user,
                title="Welcome to the platform!",
                description="Your account has been successfully created. Start exploring our features now.",
                type="message",
                url="",
                is_unread=True,
            )
            print("Notification created")
            return redirect('home')
        else:
            print("Form is invalid")
            # 收集错误信息
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field.capitalize()}: {error}")

    # 将错误信息传递给模板
    return render(request, 'users/signup.html', {'form': form, 'error_messages': error_messages})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')  # Redirect to home page or another page
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to login page
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
    # 确保用户的 Profile 存在
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # 保存数据并显示成功消息
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            # 如果表单无效，显示错误消息
            messages.error(request, 'Please correct the errors below.')
    else:
        # 初始化表单实例
        form = UserProfileForm(instance=profile)

    # 渲染更新页面
    return render(request, 'users/update_profile.html', {'form': form})


@login_required


def dashboard(request):
    # 从 EducationalContent 表中获取所有视频内容
    all_videos = EducationalContent.objects.filter(content_type="Video")
    
    # 随机选择一个视频
    random_video = random.choice(all_videos) if all_videos.exists() else None
    mood_logs = request.user.mood_logs.order_by('-timestamp')

    daily_challenges = ChallengeTemplate.objects.filter(category='Daily')[:3]  # 示例：每日挑战
    user_badges = Badge.objects.filter(user=request.user)  # 用户徽章

    return render(request, 'users/pages/dashboard.html', {
        "active_menu": "Dashboard",
        "random_video": random_video,
        "mood_logs": mood_logs,
        "daily_challenges": daily_challenges,
        "user_badges": user_badges,
    })


@login_required
def mood_tracking(request):
    mood_logs = MoodLog.objects.filter(user=request.user).order_by('-timestamp')

    if request.method == 'POST':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.save()
            return redirect('mood_tracking')
    else:
        form = MoodLogForm()

    return render(request, 'users/pages/mood_tracking.html', {
        'active_menu': 'MoodTracking',
        'form': form,
        'mood_logs': mood_logs,
    })

@login_required
def video_recommendations(request):
    try:
        contents = list(EducationalContent.objects.all())  # 强制加载 QuerySet
        print(f"Contents count in view: {len(contents)}")
    except Exception as e:
        print(f"Error querying EducationalContent: {e}")
    return render(request, 'users/pages/video_recommendations.html', {
        "active_menu": "VideoRecommendations",
        "contents": contents,
    })

@login_required
def consultation(request):
    """Consultation 视图"""
    return render(request, 'users/pages/consultation.html', {
        "active_menu": "AIConsultation",  # 动态高亮侧边栏菜单项
    })

@login_required
def gamification(request):
    """
    Gamification 首页视图函数
    """
    # 从模型中获取每日挑战和徽章信息
    today_challenge = DailyChallenge.objects.filter(user=request.user, date_assigned=date.today()).first()
    user_badges = Badge.objects.filter(user=request.user)

    # 渲染模板并传递数据
    return render(request, 'users/pages/gamification.html', {
        "active_menu": "Gamification",  # 动态高亮侧边栏菜单项
        'challenge': today_challenge,
        'badges': user_badges,
    })