from django.db import models
from django.urls import reverse
from mapa.models import Mapa
from djgeojson.fields import PointField


class Kategoria(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poszukiwania:rzeczy_list_by_category', args=[self.slug])


class Rzeczy(models.Model):
    location = models.OneToOneField(Mapa, on_delete=models.CASCADE, primary_key=True)
    kategoria = models.ForeignKey(Kategoria, related_name='rzeczy', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='publish')
    year = models.PositiveIntegerField(blank=True, default=1900)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='rzeczy/%Y/%m/%d', blank=True)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def Content(self):
        return '<img src="{}">'.format(self.image.url)

    def get_absolute_url(self):
        return reverse('poszukiwania:rzecz_detail', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug,
                                                          self.pk])



