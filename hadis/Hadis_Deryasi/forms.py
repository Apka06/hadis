from django import forms
from .models import FavoritesHadis, FavoritesWord

class FavoritesHadisForm(forms.ModelForm):
    class Meta:
        model = FavoritesHadis
        fields = ['number', 'content']

class FavoritesWordForm(forms.ModelForm):
    class Meta:
        model = FavoritesWord
        fields = ['number', 'word']