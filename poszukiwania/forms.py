from django import forms
from django.contrib.auth.models import User
from django.contrib.gis import forms as gis
from .models import Rzeczy, Mapa


class RzeczyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RzeczyForm, self).__init__( *args, **kwargs)
        self.fields['name'].label = ''
        self.fields['year'].label = ''
        self.fields['text'].label = ''

    class Meta:
        model = Rzeczy
        fields = ('category', 'name', 'slug', 'year', 'text', 'image_obverse', 'image_reverse')
        widgets = {
            'category': forms.Select(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'slug': forms.HiddenInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'text'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'image_obverse': forms.FileInput(attrs={'class': 'form-control'}),
            'image_reverse': forms.FileInput(attrs={'class': 'form-control'}),
        }


class MapaForm(gis.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MapaForm, self).__init__(*args, **kwargs)
        self.fields['geolocation'].label = ''

    class Meta:
        model = Mapa

        fields = ('geolocation',)
        widgets = {'geolocation': gis.OSMWidget(attrs={'map_height': 580,'template_name': 'gis/openlayers-osm.html',
                   'default_lat': 52.012,
                   'default_lon':21.922,
                   'default_zoom': 13,
                   })}


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'class': 'register_input'}))
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput(attrs={'class': 'register_input'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input'})}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']
