# from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http.response import Http404
# from utils.recipes.factory import make_recipe
# from django.http import Http404
from django.db.models import Q      # >> usado para consultas complexas no django
from django.core.paginator import Paginator
from utils.pagination import make_pagination

from recipes.models import Recipe

import os
PER_PAGE = int(os.environ.get('PER_PAGE', 6))
# print(PER_PAGE, type(PER_PAGE))


# Create your views here.

def home(request):  # noqa: E302
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    # current_page = request.GET.get('page', 1)
    # try:
    #     current_page = int(request.GET.get('page', 1))
    # except ValueError:
    #     current_page = 1
    # paginator = Paginator(recipes, 9)
    # page_obj = paginator.get_page(current_page)

    # pagination_range = make_pagination_range(
    #     paginator.page_range,
    #     4,
    #     current_page,
    # )
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        # 'recipes': recipes,
        'recipes': page_obj,
        'pagination_range': pagination_range,
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

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        # 'recipes': recipes,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
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
