import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from ..models import Notification

@login_required
def notifications_view(request):
    """
    View for displaying user notifications.
    """
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    unread_count = Notification.objects.filter(user=request.user, is_unread=True).count()
    context = {
        'notifications': user_notifications,
        'unread_count': unread_count,
    }
    return render(request, 'users/notifications.html', context)


@require_POST
@login_required
def mark_all_read(request):
    """
    Mark all notifications as read for the current user.
    """
    try:
        notifications = Notification.objects.filter(user=request.user, is_unread=True)
        notifications.update(is_unread=False)
        unread_count = 0
        return JsonResponse({'success': True, 'unread_count': unread_count})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@require_POST
@login_required
def mark_as_read(request):
    """
    Mark a single notification as read.
    """
    try:
        # Parse JSON data from the request body
        data = json.loads(request.body)
        notification_id = data.get('notification_id')

        if not notification_id:
            return JsonResponse({'success': False, 'error': 'Invalid notification ID'})

        # Fetch the notification and mark it as read
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_unread = False
        notification.save()

        # Get updated unread count
        unread_count = Notification.objects.filter(user=request.user, is_unread=True).count()

        return JsonResponse({'success': True, 'unread_count': unread_count})
    except Notification.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Notification not found'})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
