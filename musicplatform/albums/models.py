from email.policy import default
from operator import mod
from pickle import TRUE
from django.db import models

from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, related_name= "albums")
    album_name = models.TextField(blank = False, unique = True)
    creation_date = models.DateTimeField(auto_now_add=True, null = False)
    release_date = models.DateTimeField(auto_now_add=True, null = False)
    cost = models.FloatField(null = False)
    approved = models.BooleanField(default = False, help_text = "Approve the album if its name is not explicit")
    def __str__(self) -> str:
        return self.album_name
