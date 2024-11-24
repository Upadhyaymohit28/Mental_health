from django.contrib import admin
from .models import EmergencyContact, ProfessionalConnection

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'phone_number')
    search_fields = ('name', 'region')

@admin.register(ProfessionalConnection)
class ProfessionalConnectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'phone_number')
    search_fields = ('name', 'specialization')