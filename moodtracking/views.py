from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from moodtracking.models import MoodLog


@login_required
def mood_history(request):
    moods = MoodLog.objects.filter(user=request.user).order_by('date')
    total_points = sum(mood.get_points() for mood in moods)
    return render(request, 'moodtracking/mood_history.html',
                  {'total_points': total_points, 'moods': moods})
