from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

from .forms import ArtistForm
import requests


def login(request):
    return render(request, 'login.html' )
