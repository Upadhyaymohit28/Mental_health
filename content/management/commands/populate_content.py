from django.core.management.base import BaseCommand
from content.models import EducationalContent


class Command(BaseCommand):
    help = 'Clean the dataset and populate the database with educational content'

    def handle(self, *args, **kwargs):
        try:
            # Step 1: Clean the dataset
            EducationalContent.objects.all().delete()
            self.stdout.write(self.style.WARNING('Existing educational content has been deleted.'))

            # Step 2: Define sample data
            samples = [
                {
                    "title": "The Benefits of Deep Breathing",
                    "body": "Learn how deep breathing exercises can reduce stress and improve overall well-being.",
                    "content_type": "Article",
                    "category": "Mental Health",
                    "source_url": "https://www.health.harvard.edu/lung-health-and-disease/learning-diaphragmatic-breathing"
                },
                {
                    "title": "Introduction to Mindful Eating",
                    "body": "Discover how mindful eating can improve your relationship with food and overall health.",
                    "content_type": "Article",
                    "category": "Physical Health",
                    "source_url": "https://www.healthline.com/nutrition/mindful-eating-guide"
                },
                {
                    "title": "Digital Detox: Reclaiming Your Time and Focus",
                    "body": "Learn strategies to reduce screen time and increase productivity.",
                    "content_type": "Article",
                    "category": "Lifestyle",
                    "source_url": "https://www.verywellmind.com/why-and-how-to-do-a-digital-detox-4771321"
                },
                {
                    "title": "Building Resilience in Challenging Times",
                    "body": "Develop skills to bounce back from adversity and grow stronger.",
                    "content_type": "Article",
                    "category": "Mental Health",
                    "source_url": "https://www.apa.org/topics/resilience"
                },
                {
                    "title": "Beginner's Guided Mindfulness Meditation (5 Minutes) No Music",
                    "body": "A short, music-free guided mindfulness meditation for beginners.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=ZToicYcHIOU"
                },
                {
                    "title": "Simple 5-Minute Guided Meditation For Beginners",
                    "body": "A beginner-friendly meditation focusing on breath awareness.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=inpok4MKVLM"
                },
                {
                    "title": "Mindfulness Meditation - Guided 10 Minutes",
                    "body": "A 10-minute guided mindfulness meditation for relaxation and focus.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=6p_yaNFSYao"
                },
                {
                    "title": "5 Min Meditation Anyone Can Do Anywhere",
                    "body": "A quick guided meditation for finding peace and recentering, suitable for beginners.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=LDs7jglje_U"
                },
                {
                    "title": "Guided Meditation for Beginners",
                    "body": "A comprehensive guided meditation session designed for newcomers to mindfulness practice.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=MRQSlqoHppI"
                },
                {
                    "title": "Beginner's Guided Mindfulness Meditation (5 Minutes) No Music",
                    "body": "A short, music-free guided mindfulness meditation for beginners focusing on breath awareness.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=KUA8EhzrHD0"
                },
                {
                    "title": "5 Minute Mindfulness Meditation",
                    "body": "A brief mindfulness practice to help center your thoughts and reduce stress.",
                    "content_type": "Video",
                    "category": "Mental Health",
                    "source_url": "https://www.youtube.com/watch?v=ssss7V1_eyA"
                }
            ]

            # Step 3: Bulk insert data
            content_objects = [
                EducationalContent(
                    title=sample["title"],
                    body=sample["body"],
                    content_type=sample["content_type"],
                    category=sample["category"],
                    source_url=sample["source_url"],
                )
                for sample in samples
            ]

            # Using bulk_create for performance improvement
            EducationalContent.objects.bulk_create(content_objects)

            self.stdout.write(self.style.SUCCESS(f"{len(samples)} educational content items populated successfully!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error populating educational content: {e}"))
