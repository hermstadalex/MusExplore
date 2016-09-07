#!/usr/bin/env python3

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

import requests
import logging

from .. import pitchfork

def results_page(request):
    """
        This is the view corresponding to the page that will appear when a user enters an artist into the search bar
    """
    logger = logging.getLogger(__name__)

    logger.info('hello')


    print (list(request.GET.items()))

    # Get whatever the user entered into the form, and store it into a variable
    artist = list(request.GET.items())[0][1]



    # Make three URLs to be requests to the Last FM API: top albums, similar artists, and top tags
    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    url2 = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'
    url3 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + artist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'

    # Make the three requests, storing the request objects in their corresponding variables
    topAlbumsRequest = requests.get( url )
    similarArtistsRequest = requests.get( url2 )
    artistGenreList = requests.get( url3 )

    # Make three empty lists for albums, similar artists, and genres, which will be passed into the template when rendered
    top_albums = []
    simArtist = []
    top_genre = []

    # First, append the main artist's genre to the genre list
    top_genre.append( artistGenreList.json()["toptags"]["tag"][0]["name"] )

    # Add the top 5 results from the top albums request to the list
    for i in range(5):
        top_albums.append(topAlbumsRequest.json()["topalbums"]["album"][i]["name"])


    # For this loop, populate both the tags array and the similar artists array 
    for j in range(3):

        # First, append the current similar artist to the simArtists array
        currSimArtist = similarArtistsRequest.json()["similarartists"]["artist"][j]["name"]
        simArtist.append( currSimArtist )

        # Construct the request URL using the current similar artist's name
        reqUrl = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist=' + currSimArtist + '&api_key=673c370b7184a43691df1c7c2b35874f&format=json'

        # Make the request
        topTagsRequest = requests.get( reqUrl )

        # Append the first tag to the tag list
        top_genre.append( topTagsRequest.json()["toptags"]["tag"][0]["name"] )
        
    artist = topAlbumsRequest.json()["topalbums"]["@attr"]["artist"]

    pitchfork_ratings = []

    # Get the pitchfork ratings of each top album
    for album in top_albums:
        search = pitchfork.search(artist, album) 

        pitchfork_ratings.append( search.score() )



    return render( request, 'results_page.html', {'top_albums': top_albums, 'simArtist': simArtist, 'artist': artist, 'top_genre': top_genre })
