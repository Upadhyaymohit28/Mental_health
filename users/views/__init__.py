from .main_views import (
    signup,
    login_user,
    logout_user,
    dashboard,
    profile,
    update_profile,
)
from .notifications import (
    notifications_view,
    mark_all_read,
    mark_as_read,
)

# 导出所有需要的视图函数
__all__ = [
    "signup",
    "login_user",
    "logout_user",
    "dashboard",
    "profile",
    "update_profile",
    "notifications_view",
    "mark_all_read",
    "mark_as_read",
]
