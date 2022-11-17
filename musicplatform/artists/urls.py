
from django.contrib import admin
from django.urls import path, include
from .views import ArtistCreate, ArtistPush, ViewArtist

urlpatterns = [
    path('', ViewArtist),
    path('create/', ArtistCreate),
    path('publish/', ArtistPush)
]
