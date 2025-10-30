from django.shortcuts import render
from django.http import HttpResponse

def inbox(request):
    return HttpResponse("<h1>Direct Messages</h1><p>Your private conversations will appear here.</p>")
