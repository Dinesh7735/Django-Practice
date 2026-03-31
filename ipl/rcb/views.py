from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>King For a Reason</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>Pattidar For a Reason</h1>')