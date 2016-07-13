from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template



def index(request):
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' )

def contact(request):
    return render(request, 'contact.html' )

def help(request):
    return render(request, 'help.html' )
