from tkinter import Widget
from django import forms
from django.forms import ModelForm

from artists.models import Artist
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError

from albums.models import Album, Song


class AlbumCreateForm(forms.Form):
    artist = forms.ModelChoiceField(queryset = Artist.objects.all())
    album_name = forms.CharField()
    creation_date = forms.DateField(help_text="Ex: 2006-10-25")
    release_date = forms.DateField()
    cost = forms.FloatField()
    approved = forms.BooleanField(help_text = "Note: Approve the album if its name is not explicit")

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields ='__all__'