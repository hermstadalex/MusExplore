from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template

import requests


def signup(request):
    return render(request, 'signup.html' )

