from django import forms
from .models import Favorites

class FavoritesForm(forms.ModelForm):
    class Meta:
        model = Favorites
        fields = ['number', 'content']

