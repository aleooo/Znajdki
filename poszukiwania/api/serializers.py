from rest_framework import serializers
from ..models import Rzeczy, Category, Map
from django.contrib.auth.models import User


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('point', 'description')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
        extra_kwargs = {
            'username': {'validators': []}
        }


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title',)
        extra_kwargs = {
            'title': {'validators': []}
        }


class FindsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location = MapSerializer()
    user = UserSerializer()

    class Meta:
        model = Rzeczy
        fields = ('pk', 'location', 'category', 'user', 'name', 'slug', 'year', 'text', 'image_obverse',
                  'image_reverse', 'comments', 'catalog_number', 'update', 'publish')
        read_only_fields = ('user',)

    # def update(self, instance, validated_data):
    #     category = validated_data.pop('category')
    #     user = validated_data.pop('user')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.year = validated_data.get('year', instance.year)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.image_obverse = validated_data.get('image_obverse', instance.image_obverse)
    #     instance.comments = validated_data.get('comments', instance.comments)
    #     instance.catalog_number = validated_data.get('catalog_number', instance.catalog_number)
    #     instance.update = validated_data.get('update', instance.update)
    #     instance.publish = validated_data.get('publish', instance.publish)
    #     instance.save()
    #
    #     category_id = category.get('id', None)
    #     if category_id:
    #         cat = Category.objects.get(id=category_id)
    #         cat.title = category.get('title', cat.title)
    #         cat.save()
    #
    #     user_id = user.get('id', None)
    #     if user_id:
    #         us = User.objects.get(id=user_id)
    #         us.username = user.get('username', us.username)
    #         us.save()
    #
    #     return instance
