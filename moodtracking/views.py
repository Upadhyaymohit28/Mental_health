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
            # 保存用户的 MoodLog 数据
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.save()
            # 返回成功状态和消息
            return JsonResponse({'success': True, 'message': "Your mood has been saved successfully!"})
        else:
            # 如果有错误，返回错误信息
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    # 如果是 GET 请求，返回完整页面
    form = MoodLogForm()
    return render(request, 'users/pages/mood_tracking.html', {
        'form': form,
    })



@login_required
def mood_history(request):
    mood_logs = request.user.mood_logs.order_by('-timestamp')
    return render(request, 'moodtracking/mood_history.html', {'mood_logs': mood_logs})

