from dataclasses import field
from pyexpat import model
import re
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Album
from django.core.exceptions import ValidationError


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
    def validate(self, attrs):
        if Album.objects.filter(name = attrs['album_name']).exists():
            raise ValidationError("This album name already exists")
        return super().validate(attrs)

