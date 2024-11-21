from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodLogForm


@login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.save()
            return redirect('mood_history')
    else:
        form = MoodLogForm()
    return render(request, 'moodtracking/log_mood.html', {'form': form})


@login_required
def mood_history(request):
    mood_logs = request.user.mood_logs.order_by('-timestamp')
    return render(request, 'moodtracking/mood_history.html', {'mood_logs': mood_logs})
