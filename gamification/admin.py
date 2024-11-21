from django.contrib import admin
from .models import Badge, Streak, DailyChallenge, ChallengeTemplate


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'awarded_at')
    search_fields = ('user__username', 'name')


@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_streak', 'longest_streak', 'last_activity_date')


@admin.register(DailyChallenge)
class DailyChallengeAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_completed', 'date_assigned')


@admin.register(ChallengeTemplate)
class ChallengeTemplateAdmin(admin.ModelAdmin):
    list_display = ('task', 'difficulty')
    search_fields = ('task',)
    list_filter = ('difficulty',)
