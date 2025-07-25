#from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from utils.recipes.factory import make_recipe 
# from django.http import Http404

from recipes.models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')    
    return render(request, 'recipes/pages/home.html', context={
        'recipes':recipes,        
    })


def category(request, category_id):    
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/category.html', context={
        'recipes':recipes,
        'title': f'{recipes[0].category.name} - Category | '
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



# def category(request, category_id):
#     recipes = Recipe.objects.filter(
#         category__id=category_id,
#         is_published=True,
#     ).order_by('-id')

#     if not recipes:
#         raise Http404('Not found 🥲')    
#     return render(request, 'recipes/pages/category.html', context={
#         'recipes':recipes,
#         'title': f'{recipes.first().category.name} - Category | '
#     })