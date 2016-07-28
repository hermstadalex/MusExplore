from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

from .forms import ArtistForm
import requests



def index(request):

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/results/')
    else:
        form = ArtistForm()

    return render(request, 'index.html', {'form': form} )




def about(request):
    return render(request, 'about.html' )

def contact(request):
    return render(request, 'contact.html' )

def help(request):
    return render(request, 'help.html' )

def signup(request):
    return render(request, 'signup.html' )

def login(request):
    return render(request, 'login.html' )

def formtest_start(request):

    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/results/')
    else:
        form = ArtistForm()

    return render(request, 'formtest.html', {'form': form} )





def results_page(request):

    artist = request.POST.items()[1][1] 
    similarArtist= request.POST.items()[1][1]

    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    url2 = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=' + similarArtist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    r = requests.get( url )
    s = requests.get(url2 )

    top_albums = []
    simArtist = []
    
    for i in range(5):
        top_albums.append(r.json()["topalbums"]["album"][i]["name"])
    for j in range(3):
        simArtist.append(s.json()["similarartists"]["artist"][j]["name"])
    artist = r.json()["topalbums"]["@attr"]["artist"]
    return render(request, 'results_page.html', {'top_albums': top_albums, 'simArtist': simArtist, 'artist': artist},) 



