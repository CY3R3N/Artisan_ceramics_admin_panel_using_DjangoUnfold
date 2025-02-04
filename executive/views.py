from rest_framework import generics
from .models import Executive
from .serializers import ExecutiveSerializer

class ExecutiveList(generics.ListCreateAPIView):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer

class ExecutiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer