from django.urls import path
from .views import DirectorboardList, DirectorDetail

urlpatterns = [
    path('directorboard/', DirectorboardList.as_view(), name='directorboard-list'),
    path('directorboard/<int:pk>/', DirectorboardDetail.as_view(), name='directorboard-detail'),
]