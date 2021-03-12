from django.db import models
from djgeojson.fields import PointField



class Mapa(models.Model):
    geolokalizacja = PointField()
    description = models.TextField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='mapa/%Y/%m/%d', blank=True)


    @property
    def popupContent(self):
      return '<img src="{}"/>'.format(self.picture.url)