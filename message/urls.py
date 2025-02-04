from django.urls import path
from .views import MessageView

urlpatterns = [
    path('api/messages', MessageView.as_view(), name = 'message-endpoint'),
]
