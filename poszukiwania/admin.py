from django.contrib import admin
from .models import Category, Rzeczy, Mapa
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin as geo


@admin.register(Mapa)
class MapaAdmin(geo.GeoModelAdmin):
    default_zoom = 19
    default_lon = 21.922
    default_lat = 52.012
    list_display = ('geolocation', 'description')

@admin.register(Category)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Rzeczy)
class RzeczyAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')
    list_filter = ('title', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
