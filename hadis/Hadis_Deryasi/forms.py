from django import forms
from .models import FavoritesHadis

class FavoritesForm(forms.ModelForm):
    class Meta:
        model = FavoritesHadis
        fields = ['number', 'content']

