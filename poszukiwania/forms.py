from django import forms
from .models import Rzeczy


class RzeczyForm(forms.Form):
    class Meta:
        model = Rzeczy
        fields = ('kategoria', 'title', 'year', 'text', 'image')