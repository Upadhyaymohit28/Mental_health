from django.core.management.base import BaseCommand
from content.models import EducationalContent

class Command(BaseCommand):
    help = 'Clean the dataset and populate the database with educational content'

    def handle(self, *args, **kwargs):
        # Step 1: Clean the dataset
        EducationalContent.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing educational content has been deleted.'))

        # Step 2: Define sample data
        samples = [
            # Mental Health
            {"title": "Mindfulness Meditation for Beginners", "body": "A guided mindfulness meditation session.", "content_type": "Video", "category": "Mental Health", "source_url": "https://www.youtube.com/watch?v=inpok4MKVLM"},
            {"title": "Understanding Anxiety", "body": "Explore the causes and coping mechanisms for anxiety.", "content_type": "Article", "category": "Mental Health", "source_url": "https://www.helpguide.org/articles/anxiety/anxiety-disorders-and-anxiety-attacks.htm"},
            {"title": "Dealing with Stress", "body": "Practical tips to manage and reduce stress effectively.", "content_type": "Article", "category": "Mental Health", "source_url": "https://www.apa.org/topics/stress/tips"},

            # Physical Health
            {"title": "10-Minute Morning Yoga Routine", "body": "A quick yoga session to kickstart your day.", "content_type": "Video", "category": "Physical Health", "source_url": "https://www.youtube.com/watch?v=4C-gxOE0j7s"},
            {"title": "Healthy Eating on a Budget", "body": "Learn how to plan nutritious meals without overspending.", "content_type": "Article", "category": "Physical Health", "source_url": "https://www.eatright.org/health/wellness/preventing-illness/eating-right-on-a-budget"},
            {"title": "Home Workout for Beginners", "body": "A beginner-friendly workout routine you can do at home.", "content_type": "Video", "category": "Physical Health", "source_url": "https://www.youtube.com/watch?v=UItWltVZZmE"},

            # Lifestyle
            {"title": "How to Create a Productive Morning Routine", "body": "Learn how to set yourself up for success each day.", "content_type": "Video", "category": "Lifestyle", "source_url": "https://www.youtube.com/watch?v=yyVAkEFiI_s"},
            {"title": "Decluttering Your Space, Declutter Your Mind", "body": "The psychological benefits of a clean and organized space.", "content_type": "Article", "category": "Lifestyle", "source_url": "https://www.becomingminimalist.com/declutter-your-mind/"},

            # Social Well-being
            {"title": "The Power of Gratitude", "body": "Learn how expressing gratitude can enhance your relationships.", "content_type": "Article", "category": "Social Well-being", "source_url": "https://www.psychologytoday.com/us/basics/gratitude"},
            {"title": "Building Strong Relationships", "body": "Key principles for building meaningful connections.", "content_type": "Video", "category": "Social Well-being", "source_url": "https://www.youtube.com/watch?v=vo_N5y2c1Cs"},

            # Miscellaneous
            {"title": "The Science of Happiness", "body": "Discover what science says about finding true happiness.", "content_type": "Video", "category": "Miscellaneous", "source_url": "https://www.youtube.com/watch?v=2xwplq4yytU"},
            {"title": "Creative Journaling for Mental Clarity", "body": "Learn how to use journaling for stress relief and creativity.", "content_type": "Article", "category": "Miscellaneous", "source_url": "https://www.bulletjournal.com/blog/journaling-for-mental-health"},
        ]

        for sample in samples:
            EducationalContent.objects.get_or_create(
                title=sample['title'],
                body=sample['body'],
                content_type=sample['content_type'],
                category=sample['category'],
                source_url=sample.get('source_url', None)
            )

        self.stdout.write(self.style.SUCCESS(f"{len(samples)} educational content items populated successfully!"))