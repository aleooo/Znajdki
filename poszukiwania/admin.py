from django.contrib import admin
from .models import Category, Rzeczy, Map


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('point', 'description',)


@admin.register(Category)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Rzeczy)
class RzeczyAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish')
    list_filter = ('name', 'publish')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
