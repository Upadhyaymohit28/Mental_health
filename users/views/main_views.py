# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ..forms import UserProfileForm
from ..models import UserProfile, Notification
from django.views.decorators.http import require_POST
from django.http import JsonResponse

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

@login_required
def dashboard(request):
    """Dashboard 视图"""
    return render(request, 'users/pages/dashboard.html', {
        "active_menu": "Dashboard",  # 高亮 Dashboard 菜单
    })

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update_profile(request):
    # Ensure the profile exists
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'users/update_profile.html', {'form': form})

