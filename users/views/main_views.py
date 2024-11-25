# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ..forms import UserProfileForm
from ..models import UserProfile, Notification
<<<<<<< HEAD
from moodtracking.models import MoodLog
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from content.models import EducationalContent
import random
from content.models import EducationalContent
from moodtracking.forms import MoodLogForm
from django.shortcuts import redirect
=======
from django.views.decorators.http import require_POST
from django.http import JsonResponse
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3

def signup(request):
    if request.method == 'POST':
        print("POST request received")
        form = UserCreationForm(request.POST)
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
            
            # 跳转到主页
            return redirect('home')
        else:
            print("Form is invalid")
    else:
        print("GET request received")
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

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

<<<<<<< HEAD
=======
@login_required
def dashboard(request):
    """Dashboard 视图"""
    return render(request, 'users/pages/dashboard.html', {
        "active_menu": "Dashboard",  # 高亮 Dashboard 菜单
    })
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
<<<<<<< HEAD
    # 确保用户的 Profile 存在
=======
    # Ensure the profile exists
>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
<<<<<<< HEAD
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

    # 从 MoodLog 表中获取用户最近的 5 条心情记录
    recent_mood_logs = MoodLog.objects.filter(user=request.user).order_by('-timestamp')[:5]

    return render(request, 'users/pages/dashboard.html', {
        "active_menu": "Dashboard",
        "random_video": random_video,  # 将随机视频传递到模板
        "recent_mood_logs": recent_mood_logs,  # 将心情记录传递到模板
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
        for content in contents:
            print(f"Title: {content.title}, Category: {content.category}, URL: {content.source_url}")
    except Exception as e:
        print(f"Error querying EducationalContent: {e}")
    return render(request, 'users/pages/video_recommendations.html', {
        "active_menu": "VideoRecommendations",
        "contents": contents,
    })

from django.shortcuts import render, get_object_or_404

def recommendation_detail(request, content_id):
    content = get_object_or_404(EducationalContent, id=content_id)
    return render(request, 'content_detail.html', {
        'content': content,
        "active_menu": "VideoRecommendations",
    })


@login_required
def consultation(request):
    """Consultation 视图"""
    return render(request, 'users/pages/consultation.html', {
        "active_menu": "AIConsultation",  # 动态高亮侧边栏菜单项
    })
=======
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'users/update_profile.html', {'form': form})

>>>>>>> 00135689df92aba2bb4bdeffae8a0291044eb1f3
