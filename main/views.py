from django.shortcuts import render, redirect
from .forms import MoodEntryForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/home.html')


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
    return render(request, 'main/add_mood.html', {'form': form})


def crisis_support(request):
    return render(request, 'main/crisis_support.html')


def resources(request):
    return render(request, 'main/resources.html')
