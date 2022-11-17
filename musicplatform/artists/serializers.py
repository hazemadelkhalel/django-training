from dataclasses import field
from pyexpat import model
import re
from xml.dom import ValidationErr
from albums.serializers import AlbumSerializer
from rest_framework import serializers
from .models import Artist
from django.core.exceptions import ValidationError


class ArtistSerializerCreation(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'social_link']
    def validate(self, attrs):
        if Artist.objects.filter(name = attrs['name']).exists():
            raise ValidationError("This artist name already exists")
        return super().validate(attrs)
class ArtistSerializerView(serializers.ModelSerializer):
    albums = AlbumSerializer(many = True)
    class Meta:
        model = Artist
        fields = ['name', 'social_link', 'albums']
