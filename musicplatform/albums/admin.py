from xml.etree.ElementTree import tostring
from django.contrib import admin

from albums.models import Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ("creation_date", )
    list_display = ('album_name', 'approved', )
    ordering = ('-approved', )
admin.site.register(Album, AlbumAdmin)

