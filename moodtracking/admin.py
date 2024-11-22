from django.contrib import admin
from .models import MoodLog

@admin.register(MoodLog)
class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood_score', 'timestamp')
    search_fields = ('user__username', 'description')
    list_filter = ('timestamp',)