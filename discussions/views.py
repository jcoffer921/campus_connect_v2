from django.shortcuts import render
from django.http import HttpResponse

def discussion_home(request):
    return HttpResponse("<h1>Discussions</h1><p>Topic threads and replies will show up here soon.</p>")
