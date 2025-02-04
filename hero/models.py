from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255, help_text="Text to overlay on the video")
    video = models.FileField(upload_to='hero_videos/', help_text="Upload the hero video")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Showcase(models.Model):
    product_image = models.ImageField(upload_to='showcase_images/', help_text="Upload Product Image")
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def recent_showcases(cls, count=5):
        return cls.objects.order_by('-created_at')[:count]
    def __str__(self):
        return f"Showcase Image {self.id}"
    
class BrandVideo(models.Model):
    title = models.CharField(max_length=255, help_text="Text to overlay on the video")
    video = models.FileField(upload_to='hero_videos/', help_text="Upload the hero video")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # Ensure your React frontend fetches data from the /hero/hero-section/ and /hero/showcase/ endpoints.