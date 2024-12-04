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
    form = UserCreationForm(request.POST or None)  
    error_messages = []

    if request.method == 'POST':
        print("POST request received")
        if form.is_valid():
            print("Form is valid")
            # Save new user
            user = form.save()
            # Log in the new user
            login(request, user)

            # Create notification
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
            # Collect error messages
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field.capitalize()}: {error}")

    # Pass error messages to the template
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
    # Ensure the user's profile exists
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # Save data and show success message
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            # If form is invalid, show error message
            messages.error(request, 'Please correct the errors below.')
    else:
        # Initialize form instance
        form = UserProfileForm(instance=profile)

    # Render update profile page
    return render(request, 'users/update_profile.html', {'form': form})

@login_required
def dashboard(request):
    # Fetch all video content from EducationalContent table
    all_videos = EducationalContent.objects.filter(content_type="Video")
    
    # Randomly select a video
    random_video = random.choice(all_videos) if all_videos.exists() else None
    mood_logs = request.user.mood_logs.order_by('-timestamp')

    daily_challenges = ChallengeTemplate.objects.filter(category='Daily')[:3]  # Example: daily challenges
    user_badges = Badge.objects.filter(user=request.user)  # User badges

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
        contents = list(EducationalContent.objects.all())  # Force load QuerySet
        print(f"Contents count in view: {len(contents)}")
    except Exception as e:
        print(f"Error querying EducationalContent: {e}")
    return render(request, 'users/pages/video_recommendations.html', {
        "active_menu": "VideoRecommendations",
        "contents": contents,
    })

@login_required
def consultation(request):
    """Consultation view"""
    return render(request, 'users/pages/consultation.html', {
        "active_menu": "AIConsultation",  # Dynamically highlight sidebar menu item
    })

@login_required
def gamification(request):
    """
    Gamification homepage view function
    """
    # Fetch daily challenges and badge information from models
    today_challenge = DailyChallenge.objects.filter(user=request.user, date_assigned=date.today()).first()
    user_badges = Badge.objects.filter(user=request.user)

    if request.method == 'POST' and 'complete_challenge' in request.POST:
        if today_challenge:
            today_challenge.is_completed = True
            today_challenge.save()

    # Render template and pass data
    return render(request, 'users/pages/gamification.html', {
        "active_menu": "Gamification",  # Dynamically highlight sidebar menu item
        'challenge': today_challenge,
        'badges': user_badges,
    })
