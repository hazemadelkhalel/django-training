import re
from django import forms

from artists.models import Artist
from django.core.exceptions import ValidationError


class ArtistCreateForm(forms.Form):
    name = forms.CharField()
    social_link = forms.CharField()
    def clean_name(self):
        if Artist.objects.filter(name = self.cleaned_data.get("name")).count() > 0:
            raise ValidationError("This artist already exists")
        else:
            return self.cleaned_data.get("name")