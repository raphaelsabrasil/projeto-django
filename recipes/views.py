#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HOME 2')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')