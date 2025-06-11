from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Raphael Sá Brasil',
    }, status=201)
