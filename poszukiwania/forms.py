from django import forms
from django.contrib.auth.models import User
from django.contrib.gis import forms as gis
from .models import Rzeczy, Mapa


class RzeczyForm(forms.ModelForm):

    class Meta:
        model = Rzeczy
        fields = ('category', 'name', 'slug', 'year', 'text', 'image_obverse', 'image_reverse', 'comments', 'catalog_number')
        widgets = {
            'category': forms.Select(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'slug': forms.HiddenInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'image_obverse': forms.FileInput(attrs={'class': 'form-control'}),
            'image_reverse': forms.FileInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'comments', 'rows': '6'}),
            'catalog_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'catalog_number'})
        }


class MapaForm(gis.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MapaForm, self).__init__(*args, **kwargs)
        self.fields['geolocation'].label = ''

    class Meta:
        model = Mapa

        fields = ('geolocation',)
        widgets = {'geolocation': gis.OSMWidget(attrs={'template_name': 'gis/openlayers-osm.html',
                   'default_lat': 52.012,
                   'default_lon':21.922,
                   'default_zoom': 13,
                   })}


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register_input'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register_input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input'}),
                   'email': forms.TextInput(attrs={'class': 'register_input'})}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['confirm_password']
