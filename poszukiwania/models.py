from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from djgeojson.fields import PointField


class Mapa(models.Model):
    geolokalizacja = PointField()


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

    @property
    def popupContent(self):
        return '<img src="{}" /><p><{}</p>'.format(
            self.image.url,
            self.text)

    def get_absolute_url(self):
        return reverse('poszukiwania:rzecz_detail', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug,
                                                          self.pk])
