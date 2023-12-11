from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ich liebe Klaudia ohne Grenza!")
# Create your views here.
