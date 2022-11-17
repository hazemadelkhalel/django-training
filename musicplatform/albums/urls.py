
from django.contrib import admin
from django.urls import path, include
from .views import AlbumPush, AlbumCreate

urlpatterns = [
    path('create/', AlbumCreate),
    path('publish/', AlbumPush)
]
