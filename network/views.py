from django.shortcuts import render
from django.http import HttpResponse

def network_home(request):
    return HttpResponse("<h1>Network Page</h1><p>Connections will appear here soon!</p>")
