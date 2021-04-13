from django.contrib import admin
from .models import Mapa
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

@admin.register(Mapa)
class MapaAdmin(LeafletGeoAdmin):
    list_display = ('geolokalizacja',)


