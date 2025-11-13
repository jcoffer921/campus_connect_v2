from django.shortcuts import render
from django.http import HttpResponse

def inbox(request):
    return render(request, 'direct_messages/direct_messages.html')