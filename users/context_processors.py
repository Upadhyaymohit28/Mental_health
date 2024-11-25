# users/context_processors.py

from .models import Notification

def notifications_processor(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        unread_count = notifications.filter(is_unread=True).count()
        return {
            'notifications': notifications,
            'unread_count': unread_count,
        }
    else:
        return {
            'notifications': [],
            'unread_count': 0,
        }
