from django.contrib import admin
from .models import Kategoria, Rzeczy, Mapa
from leaflet.admin import LeafletGeoAdmin


@admin.register(Mapa)
class MapaAdmin(LeafletGeoAdmin):
    list_display = ('geolokalizacja',)

@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Rzeczy)
class RzeczyAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')
    list_filter = ('title', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
