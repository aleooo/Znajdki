from django.db import models
from djgeojson.fields import PointField
#from django.contrib.gis.db import models


class Mapa(models.Model):
    geolokalizacja = PointField()
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='rzeczy/%Y/%m/%d', blank=True)

'''
class Mapa(models.Model):
    point = models.PointField()
'''