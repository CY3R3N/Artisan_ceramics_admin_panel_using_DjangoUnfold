from rest_framework import generics
from .models import Directorboard
from .serializers import DirectorboardSerializer

class DirectorboardList(generics.ListCreateAPIView):
    queryset = Directorboard.objects.all()
    serializer_class = DirectorboardSerializer

class DirectorboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Directorboard.objects.all()
    serializer_class = DirectorboardSerializer