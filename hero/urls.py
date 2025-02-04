from django.urls import path
from .views import HeroSectionView, ShowcaseView, BrandVideoView

urlpatterns = [
    path('hero-section/', HeroSectionView.as_view(), name='hero-section'),
    path('showcase/', ShowcaseView.as_view(), name='showcase'),
    path('brand-video/', BrandVideoView.as_view(), name='brand-video'),
]
