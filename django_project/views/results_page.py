from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

import requests

def results_page(request):

    artist = request.GET.items()[0][1]



    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    url2 = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    url3 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'

    r = requests.get( url )
    s = requests.get( url2 )
    currArtist_genre = requests.get( url3 )

    top_albums = []
    simArtist = []
    top_genre = []

    for i in range(5):
        top_albums.append(r.json()["topalbums"]["album"][i]["name"])
    for j in range(3):
        simArtist.append(s.json()["similarartists"]["artist"][j]["name"])
        url4 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
        url5 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
        url6 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
        simArtist1_genre = requests.get( url4 )
        simArtist2_genre = requests.get( url5 )
        simArtist3_genre = requests.get( url6 )

    for k in range(1):
        top_genre.append(currArtist_genre.json()["toptags"]["tag"][k]["name"])

    for l in range(3):
        top_genre.append(simArtist1_genre.json()["toptags"]["tag"][l]["name"])
        top_genre.append(simArtist2_genre.json()["toptags"]["tag"][l]["name"])
        top_genre.append(simArtist3_genre.json()["toptags"]["tag"][l]["name"])


    artist = r.json()["topalbums"]["@attr"]["artist"]
    return render(request, 'results_page.html', {'top_albums': top_albums, 'simArtist': simArtist, 'artist': artist, 'top_genre': top_genre},)


