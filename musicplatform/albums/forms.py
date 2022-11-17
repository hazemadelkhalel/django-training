from tkinter import Widget
from django import forms

from artists.models import Artist
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError

from albums.models import Album


class AlbumCreateForm(forms.Form):
    artist = forms.ModelChoiceField(queryset = Artist.objects.all())
    album_name = forms.CharField()
    creation_date = forms.DateField(help_text="Ex: 2006-10-25")
    release_date = forms.DateField()
    cost = forms.FloatField()
    approved = forms.BooleanField(help_text = "Note: Approve the album if its name is not explicit")
    def clean_album_name(self):
        print("Hahah")
        if Album.objects.filter(album_name = self.cleaned_data.get("album_name")).count() > 0:
            raise ValidationError("This album already exists")
        else:
            return self.cleaned_data.get("album")