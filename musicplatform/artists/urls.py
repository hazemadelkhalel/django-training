
from django.contrib import admin
from django.urls import path, include
from .views import ArtistCreate, ArtistView

urlpatterns = [
    path('', ArtistView.as_view()),
    path('create/', ArtistCreate.as_view()),
]
