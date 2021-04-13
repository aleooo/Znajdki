from django.db import models
from djgeojson.fields import PointField
#from django.contrib.gis.db import models


class Mapa(models.Model):
    geolokalizacja = PointField()


'''
class Mapa(models.Model):
    point = models.PointField()
'''