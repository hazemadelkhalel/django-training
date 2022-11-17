import pytest,datetime
from users.models import UserProfile

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_add_artist_with_auth(client):
    request = client.post('/artists/create/', {
        'name': 'new artist',
        'social_link':'https://www.facebook.com/',
        }, format='json', headers= {'Authorization' : 'TOK:0df75c0357541422e2003f31ea05d977d2c5ba32fb578e41696b4719a8f86d17'})
    assert request.status_code == 201

@pytest.mark.django_db
def test_add_artist_without_auth():
    client = APIClient()
    request = client.post('/artists/create/', {
        'name': 'new artist',
        'social_link':'https://www.facebook.com/',
        }, format='json')
    assert request.status_code == 201