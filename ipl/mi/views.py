from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Hitman For a Reason</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>Sky For a Reason</h1>')
