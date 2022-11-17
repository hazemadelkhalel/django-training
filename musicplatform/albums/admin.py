import imp
from pyexpat import model
from xml.etree.ElementTree import tostring
from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .forms import SongForm

from albums.models import Album, Song

class SongAdmin(admin.ModelAdmin):
    exclude = ['']
    model = SongForm

class AlbumInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise forms.ValidationError('Album must have at least one song')

# Register your models here.

class AlbumInline(admin.StackedInline):
    model = Song    
    exclude = ['']
    formset = AlbumInlineFormset

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ("creation_date", )
    list_display = ('album_name', 'approved', )
    ordering = ('-approved', )
    exclude = ['']
    inlines= (AlbumInline,)
    def clean(self):
        raise ValidationError("Album should has at least one song")

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)


