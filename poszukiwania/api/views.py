from rest_framework import generics
from ..models import Rzeczy
from .serializers import RzeczySerializer


class RzeczyListView(generics.ListAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = RzeczySerializer


class RzeczyDetailView(generics.RetrieveAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = RzeczySerializer