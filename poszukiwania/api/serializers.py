from rest_framework import serializers
from ..models import Rzeczy


class RzeczySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rzeczy
        fields = ('pk', 'category', 'name', 'slug', 'year', 'text', 'catalog_number')