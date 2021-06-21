from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


class Mapa(models.Model):
    geolocation = PointField(null=True, srid=4326)
    description = models.TextField(blank=True, default='Znajdka')

    @property
    def lat_lng(self):
        return list(getattr(self.geolocation, 'coords', [])[::-1])

    @property
    def description_f(self):
        return '{}'.format(
          self.description)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poszukiwania:objects_list_by_category', args=[self.slug])


class Rzeczy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='test')
    location = models.OneToOneField(Mapa, on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, related_name='rzeczy', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='publish', blank=True)
    year = models.PositiveIntegerField(blank=True)
    text = models.TextField(blank=True)
    image_obverse = models.ImageField('image_obverse', upload_to='rzeczy/%Y/%m/%d', default='empty.png')
    image_reverse = models.ImageField('image_revers', upload_to='rzeczy/%Y/%m/%d', default='empty.png')
    update = models.DateField(auto_now=True)
    publish = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['publish']

    def get_absolute_url(self):
        return reverse('poszukiwania:object_detail', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug,
                                                          self.pk])

