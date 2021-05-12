from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


class Mapa(models.Model):
    geolokalizacja = PointField(null=True, srid=4326)
    description = models.TextField(blank=True, default='Znajdka')

    @property
    def lat_lng(self):
        return list(getattr(self.geolokalizacja, 'coords', [])[::-1])

    @property
    def opis(self):
        return '<p>{}</p>'.format(
          self.description)
        # <img src = "{}" / >
        # self.picture.url,

class Kategoria(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poszukiwania:rzeczy_list_by_category', args=[self.slug])


class Rzeczy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='test')
    location = models.OneToOneField(Mapa, on_delete=models.CASCADE, primary_key=True)
    kategoria = models.ForeignKey(Kategoria, related_name='rzeczy', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='publish', blank=True)
    year = models.PositiveIntegerField(blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='rzeczy/%Y/%m/%d', blank=True)
    publish = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['publish']

    def get_absolute_url(self):
        return reverse('poszukiwania:rzecz_detail', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug,
                                                          self.pk])
