from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Rzeczy, Map


class RzeczyForm(forms.ModelForm):

    class Meta:
        model = Rzeczy
        fields = ('category', 'name', 'slug', 'year', 'text', 'image_obverse', 'image_reverse', 'comments', 'catalog_number')
        widgets = {
            'category': forms.Select(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('name')}),
            'slug': forms.HiddenInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('description')}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('year')}),
            'image_obverse': forms.FileInput(attrs={'class': 'form-control'}),
            'image_reverse': forms.FileInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('comments'), 'rows': '6'}),
            'catalog_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('catalog_number')}),
        }


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ('point',)
        widgets = {'point': forms.TextInput(attrs={'class': 'json_form'})}

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
            raise forms.ValidationError(_('Passwords do not match'))
        return cd['confirm_password']
