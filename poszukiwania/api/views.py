from rest_framework import generics
from ..models import Rzeczy, Category
from .serializers import RzeczySerializer, CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RzeczyListView(generics.ListAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = RzeczySerializer


class RzeczyDetailView(generics.RetrieveAPIView):
    queryset = Rzeczy.objects.all()
    serializer_class = RzeczySerializer
