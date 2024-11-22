from django.contrib import admin
from .models import EducationalContent

@admin.register(EducationalContent)
class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'category', 'created_at')
    search_fields = ('title', 'category', 'content_type')
    list_filter = ('content_type', 'category', 'created_at')