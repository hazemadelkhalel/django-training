
from django.contrib import admin
from django.urls import path, include
from .views import AlbumCreate

urlpatterns = [
    path('create/', AlbumCreate.as_view()),
]
