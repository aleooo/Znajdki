from rest_framework import serializers
from ..models import Rzeczy, Category, Mapa


class MapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mapa
        fields = ('geolocation',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)


class RzeczySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = MapSerializer()

    class Meta:
        model = Rzeczy
        fields = ('pk', 'category', 'location', 'name', 'slug', 'year', 'text', 'catalog_number')
