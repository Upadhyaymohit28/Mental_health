# main_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'main_app/home.html')

def signup(request):
    if request.method == 'POST':
        print("POST request received")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print("Form is invalid")
    else:
        print("GET request received")
        form = UserCreationForm()
    return render(request, 'main_app/signup.html', {'form': form})



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
    return render(request, 'main_app/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

from .models import MoodEntry
from .forms import MoodEntryForm
from django.contrib.auth.decorators import login_required

@login_required
def add_mood(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('mood_history')
    else:
        form = MoodEntryForm()
    return render(request, 'main_app/add_mood.html', {'form': form})

@login_required
def mood_history(request):
    moods = MoodEntry.objects.filter(user=request.user).order_by('-date')
    total_points = sum(mood.get_points() for mood in moods)
    return render(request, 'main_app/mood_history.html', {'moods': moods})

def crisis_support(request):
    return render(request, 'main_app/crisis_support.html')
def resources(request):
    return render(request, 'main_app/resources.html')
