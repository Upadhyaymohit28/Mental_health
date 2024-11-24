from django.shortcuts import render
from .models import EmergencyContact, ProfessionalConnection

def support_resources(request):
    emergency_contacts = EmergencyContact.objects.all()
    professional_connections = ProfessionalConnection.objects.all()
    return render(request, 'support/support_resources.html', {
        'emergency_contacts': emergency_contacts,
        'professional_connections': professional_connections,
    })