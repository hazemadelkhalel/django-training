import pytest,datetime
from users.models import UserProfile

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from artists.models import Artist
import json

@pytest.mark.django_db
def test_add_album_without_auth():
    client = APIClient()
    artist = Artist.objects.all().filter(name = "Amr Diab")
    request = client.post('/albums/create/', {
        'album_name': 'new album',
        'cost': 15,
        'approved':'True',
        'artist' : artist
        }, format='json')
    assert request.status_code == 201