from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest

@pytest.fixture
def auth_client(user = None):
    if(user is None):
        user = User.objects.create()
    client = APIClient()
    client.login(username=user.username, password=user.password)
    return client