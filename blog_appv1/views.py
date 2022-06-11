from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("heloo hii kaise ho")