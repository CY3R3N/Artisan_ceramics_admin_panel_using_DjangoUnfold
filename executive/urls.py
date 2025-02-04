from django.urls import path
from .views import ExecutiveList, ExecutiveDetail

urlpatterns = [
    path('executive/', ExecutiveList.as_view(), name='executive-list'),
    path('executive/<int:pk>/', ExecutiveDetail.as_view(), name='executive-detail'),
]