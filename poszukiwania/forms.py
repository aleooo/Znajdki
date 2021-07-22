from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _

from .models import Rzeczy, Map


class RzeczyForm(forms.ModelForm):
    class Meta:
        model = Rzeczy
        fields = ('category', 'name', 'slug', 'year', 'text', 'image_obverse', 'image_reverse', 'comments',
                  'catalog_number')
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


class EmailForm(validators.EmailValidator):
    message = _('Enter a valid email address.')


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input'}),
                   'email': forms.TextInput(attrs={'class': 'register_input'}),
                   'password1': forms.TextInput(attrs={'class': 'register_input'}),
                   'password2': forms.TextInput(attrs={'class': 'register_input'})}

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
