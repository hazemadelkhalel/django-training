from email.policy import default
from operator import mod
from pickle import TRUE
from statistics import mode
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

class Song(models.Model):
   album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name = 'songs')
   name = models.CharField(max_length = 255,default = album.name)
   audio = models.FileField(upload_to='songs/',help_text=("Allowed type - .mp3, .wav"))
   image = models.ImageField(upload_to='images/',default='images/def.jpg')
   def delete(self, *args, **kwargs):
      if Song.objects.filter(album = self.album).count() == 1:
         raise Exception('You can`t delete song "'+ self.name +'" because it`s only song on her album "' + self.album.album_name+'"')  # or you can throw your custom exception here.
      super(Song, self).delete(*args, **kwargs)

