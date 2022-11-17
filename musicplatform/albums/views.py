import re
from telnetlib import STATUS
from django.shortcuts import HttpResponse, render
from requests import Response
from .forms import AlbumCreateForm
from django.views.decorators.csrf import csrf_protect
from .models import Album
# Create your views here.
from .models import Artist

@csrf_protect
def AlbumCreate(response):
    form = AlbumCreateForm()
    return render(response, "createAlbum.html", {'form' : form})

@csrf_protect
def AlbumPush(request):
    form = AlbumCreateForm()
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            Album.objects.create(album_name = request.POST['album_name'], artist = Artist.objects.get(id = request.POST['artist']), 
            creation_date = request.POST['creation_date'],  release_date = request.POST['release_date']
            , cost = request.POST['cost'],  approved = True if request.POST['approved'] == 'on' else False)
            return render(request, "viewArtist.html", {'artist_list': Artist.objects.all()})
    return render(request, "createAlbum.html", {'form': form})

