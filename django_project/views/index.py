from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

from .forms import ArtistForm
import requests

from ipware.ip import get_real_ip

from django.contrib.gis.geoip import GeoIP

def index(request):

    if request.method == 'GET':
        form = ArtistForm()
        if form.is_valid():
            return HttpResponseRedirect('/results/')
    else:
        form = ArtistForm()

    return render(request, 'index.html', {'form': form} )
