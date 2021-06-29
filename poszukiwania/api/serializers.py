from rest_framework import serializers
from ..models import Rzeczy, Category, Mapa
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapa
        fields = ('geolocation',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title',)


class FindsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = MapSerializer()
    user = UserSerializer()

    class Meta:
        model = Rzeczy
        fields = ('pk', 'user', 'category', 'location', 'name', 'slug', 'year', 'text', 'image_obverse', 'image_reverse', 'comments', 'catalog_number', 'update', 'publish')
