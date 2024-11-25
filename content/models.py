from django.db import models

class EducationalContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('Article', 'Article'),
        ('Video', 'Video'),
    ]

    title = models.CharField(max_length=200)
    body = models.TextField()
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES, default='Article')
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    source_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'content'  # 将 'content' 替换为实际的 app 名称
