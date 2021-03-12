from django.contrib import admin
from .models import Mapa
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Mapa, LeafletGeoAdmin)
