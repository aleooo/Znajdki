from django import forms
from django.contrib.auth.models import User
from django.contrib.gis import forms as gis
from .models import Rzeczy, Mapa


class RzeczyForm(forms.ModelForm):
    class Meta:
        model = Rzeczy
        fields = ('kategoria', 'title', 'slug', 'year', 'text', 'image',)


class MapaForm(gis.ModelForm):
    class Meta:
        model = Mapa

        fields = ('geolokalizacja',)
        widgets = {'geolokalizacja': gis.OSMWidget(
        attrs={'map_width': 500, 'map_height': 512,'template_name': 'gis/openlayers-osm.html',
                   'default_lat': 52.012,
                   'default_lon':21.922,
                    'default_zoom': 13,
                   })}


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']
