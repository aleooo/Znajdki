from django import forms
from django.contrib.auth.models import User

from .models import Rzeczy, Mapa


class RzeczyForm(forms.ModelForm):
    class Meta:
        model = Rzeczy
        fields = ('kategoria', 'title', 'slug', 'year', 'text', 'image',)


class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa

        fields = ('geolokalizacja',)
        widgets = {'geolokalizacja': forms.HiddenInput(attrs={
            'required': False
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
