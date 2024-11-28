from django.core.management.base import BaseCommand
from content.models import EducationalContent
import requests
from bs4 import BeautifulSoup


def get_youtube_video_info(url):
    """爬取 YouTube 视频的信息，包括标题、描述和封面图"""
    if 'youtube.com' in url or 'youtu.be' in url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取封面图、标题和描述
            thumbnail_url = soup.find('meta', {'property': 'og:image'})['content'] if soup.find('meta', {'property': 'og:image'}) else None
            title = soup.find('meta', {'name': 'title'})['content'] if soup.find('meta', {'name': 'title'}) else None
            description = soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else None

            return title, description, thumbnail_url
        except Exception as e:
            print(f"Error fetching YouTube info for {url}: {e}")
            return None, None, None
    return None, None, None

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

            content_objects = []

            for sample in samples:
                youtube_title = None
                youtube_description = None
                youtube_thumbnail = None

                if sample["content_type"] == "Video":
                    # 获取 YouTube 信息
                    youtube_title, youtube_description, youtube_thumbnail = get_youtube_video_info(sample["source_url"])

                # 创建对象
                content_objects.append(
                    EducationalContent(
                        title=youtube_title if youtube_title else sample["title"],
                        body=youtube_description if youtube_description else sample["body"],
                        content_type=sample["content_type"],
                        category=sample["category"],
                        source_url=sample["source_url"],
                        youtube_title=youtube_title,
                        youtube_description=youtube_description,
                        youtube_thumbnail=youtube_thumbnail,
                    )
                )

            # 使用 bulk_create 插入数据
            EducationalContent.objects.bulk_create(content_objects)

            self.stdout.write(self.style.SUCCESS(f"{len(samples)} educational content items populated successfully!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error populating educational content: {e}"))