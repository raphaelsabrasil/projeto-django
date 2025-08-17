# from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http.response import Http404
# from utils.recipes.factory import make_recipe
# from django.http import Http404
from django.db.models import Q      # >> usado para consultas complexas no django

from recipes.models import Recipe

# Create your views here.

def home(request):  # noqa: E302
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    # recipe = Recipe.objects.filter(
    #     pk=id,
    #     is_published=True,
    # ).order_by('-id').first()
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()  # strip >> função python para remover espaços

    # caso procure vazio, levanta erro 404
    if not search_term:
        raise Http404()

    # procurar entre os titulos OU descrições a palavra digitada no campo search
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes,
    })


# def home(request):
#     return render(request, 'recipes/pages/home.html', context={
#         'recipes': [make_recipe() for _ in range(10)],  #list comprehension que gera 10 receitas, sem variável    # noqa: E501
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
