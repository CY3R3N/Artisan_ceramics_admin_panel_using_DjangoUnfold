from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inbox
from .serializers import InboxSerializer
# Create your views here.
# class InboxListView(generics.ListAPIView):
#     queryset = Inbox.objects.all()
#     serializer_class = InboxSerializer
    
# class InboxDetailView(generics.RetrieveAPIView):
#     queryset = Inbox.objects.all()
#     serializer_class = InboxSerializer
    
class MessageView(APIView):
    def post(self, request):
        serializer = InboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Message submitted successfully!"},serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)