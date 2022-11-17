import re
from unicodedata import name
from django.contrib import admin

from artists.models import Artist
from albums.models import Album

# Register your models here.
class AlbumInline(admin.TabularInline):
    model = Album
class ArtistAdmin(admin.ModelAdmin):
    def Number_of_Approved_Albums(self, obj):
        return Album.objects.all().filter(artist = obj.id , approved = True).count()
    inlines = [AlbumInline]
    list_display = ('name', 'Number_of_Approved_Albums',  )
admin.site.register(Artist, ArtistAdmin)
