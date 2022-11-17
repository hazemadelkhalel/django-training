import re
from telnetlib import STATUS
from django.shortcuts import HttpResponse, render, redirect
from requests import Response
from .forms import ArtistCreateForm
from django.views.decorators.csrf import csrf_protect
from .models import Artist
from django.core.exceptions import ValidationError
from django.contrib import messages, contenttypes

# Create your views here.

@csrf_protect
def ArtistCreate(request):
    form = ArtistCreateForm()
    return render(request, "createArtist.html", {'form' : form})

@csrf_protect
def ArtistPush(request):
    form = ArtistCreateForm()
    if request.method == 'POST':
        form = ArtistCreateForm(request.POST)
        if form.is_valid():
            Artist.objects.create(name = request.POST['name'], social_link = request.POST['social_link'])
            return render(request, "viewArtist.html", {'artist_list': Artist.objects.all()})
    return render(request, "createArtist.html", {'form': form})

def ViewArtist(request):
    return render(request, "viewArtist.html", {'artist_list': Artist.objects.all()})

