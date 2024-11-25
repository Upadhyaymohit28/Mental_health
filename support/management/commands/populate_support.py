from django.core.management.base import BaseCommand
from support.models import EmergencyContact, ProfessionalConnection

class Command(BaseCommand):
    help = 'Clean the dataset and populate with emergency contacts and professional connections'

    def handle(self, *args, **kwargs):
        EmergencyContact.objects.all().delete()
        ProfessionalConnection.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing emergency contacts and professional connections have been deleted.'))

        # Emergency Contacts
        emergency_contacts = [
            {
                "name": "Mental Health Helpline",
                "phone_number": "1-800-123-4567",
                "description": "24/7 support for mental health crises",
                "region": "Canada"
            },
            {
                "name": "Suicide Prevention Hotline",
                "phone_number": "1-800-273-8255",
                "description": "Available 24/7 to help with suicidal thoughts",
                "region": "USA"
            },
            {
                "name": "Domestic Violence Hotline",
                "phone_number": "1-800-799-7233",
                "description": "Confidential support for domestic violence victims",
                "region": "USA"
            },
            {
                "name": "Crisis Text Line",
                "phone_number": "Text HOME to 741741",
                "description": "Free crisis support via text, available 24/7",
                "region": "USA & Canada"
            },
            {
                "name": "Kids Help Phone",
                "phone_number": "1-800-668-6868",
                "description": "Confidential and professional support for youth",
                "region": "Canada"
            },
            {
                "name": "National Eating Disorders Association Helpline",
                "phone_number": "1-800-931-2237",
                "description": "Support for eating disorders and body image issues",
                "region": "USA"
            }
        ]

        for contact in emergency_contacts:
            EmergencyContact.objects.get_or_create(
                name=contact['name'],
                phone_number=contact['phone_number'],
                description=contact['description'],
                region=contact['region']
            )

        # Professional Connections
        professional_connections = [
            {
                "name": "Dr. Alice Johnson",
                "specialization": "Therapist",
                "email": "alice.johnson@example.com",
                "phone_number": "1-800-555-6789",
                "website": "",
                "description": "Specializes in anxiety and stress management"
            },
            {
                "name": "Calm Minds Counseling",
                "specialization": "Counseling Center",
                "email": "",
                "phone_number": "",
                "website": "https://calmminds.com",
                "description": "Offers affordable counseling services"
            },
            {
                "name": "BetterHelp Online Therapy",
                "specialization": "Online Therapist Network",
                "email": "",
                "phone_number": "",
                "website": "https://www.betterhelp.com",
                "description": "Connect with licensed therapists online"
            },
            {
                "name": "Dr. Emily Carter",
                "specialization": "Child Psychologist",
                "email": "emily.carter@childhelp.org",
                "phone_number": "1-800-555-1234",
                "website": "",
                "description": "Focuses on child and adolescent mental health"
            },
            {
                "name": "Open Path Collective",
                "specialization": "Therapy Network",
                "email": "",
                "phone_number": "",
                "website": "https://openpathcollective.org",
                "description": "Provides affordable therapy options nationwide"
            },
            {
                "name": "Dr. Michael Lee",
                "specialization": "Marriage and Family Therapist",
                "email": "michael.lee@familytherapist.com",
                "phone_number": "1-800-777-4567",
                "website": "",
                "description": "Specializes in family and relationship counseling"
            }
        ]

        for professional in professional_connections:
            ProfessionalConnection.objects.get_or_create(
                name=professional['name'],
                specialization=professional['specialization'],
                email=professional['email'],
                phone_number=professional['phone_number'],
                website=professional['website'],
                description=professional['description']
            )

        self.stdout.write(self.style.SUCCESS("Emergency contacts and professional connections populated successfully!"))