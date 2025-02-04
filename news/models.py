from django.db import models

# Create your models here.
class News(models.Model):
    NEWS_TYPE = [
        ('News', 'News'),
        ('Event','Event'),
    ]
    
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=32, choices= NEWS_TYPE, verbose_name="News Type")
    short_description = models.TextField(max_length=200)
    long_description = models.TextField(verbose_name="Long Description")
    news_image = models.ImageField(upload_to='news_images/', help_text="Upload News Image")
    created_at = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def recent_news(cls, count=3):
        return cls.objects.order_by('-created_at')[:count]
    
    def __str__(self):
        return self.title