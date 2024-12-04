from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import MoodLogForm

@login_required
def log_mood(request):
    """
    Handle mood logging requests via POST and refresh the form on the same page.
    """
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            # Save the user's MoodLog data
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.save()
            # Return success status and message
            return JsonResponse({'success': True, 'message': "Your mood has been saved successfully!"})
        else:
            # If there are errors, return error messages
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    # If the request is GET, return the full page
    form = MoodLogForm()
    return render(request, 'users/pages/mood_tracking.html', {
        'form': form,
    })


@login_required
def mood_history(request):
    # Retrieve mood logs for the logged-in user, ordered by timestamp (most recent first)
    mood_logs = request.user.mood_logs.order_by('-timestamp')
    return render(request, 'moodtracking/mood_history.html', {'mood_logs': mood_logs})
