#from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe 

from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes':recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes':recipes,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


# def home(request):
#     return render(request, 'recipes/pages/home.html', context={
#         'recipes': [make_recipe() for _ in range(10)],  #list comprehension que gera 10 receitas, sem variável
#     }, status=201)