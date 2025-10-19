# from django.http import HttpResponse
# from utils.recipes.factory import make_recipe
# from django.http import Http404
# from django.shortcuts import get_object_or_404, render
from django.http.response import Http404
from django.db.models import Q      # >> usado para consultas complexas no django
from django.core.paginator import Paginator
# from django.contrib import messages
from django.views.generic import DetailView, ListView
from utils.pagination import make_pagination

from recipes.models import Recipe

import os
PER_PAGE = int(os.environ.get('PER_PAGE', 6))
# print(PER_PAGE, type(PER_PAGE))


# Create your views here.

class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('recipes'),
            PER_PAGE
        )
        ctx.update(
            {'recipes': page_obj, 'pagination_range': pagination_range}
        )
        return ctx

class RecipeListViewHome(RecipeListViewBase):
    template_name = 'recipes/pages/home.html'

class RecipeListViewCategory(RecipeListViewBase):
    template_name = 'recipes/pages/category.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'title': f'{ctx.get("recipes")[0].category.name} - Category | '
        })

        return ctx

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id')
        )        
    
        if not qs:
            raise Http404()
        
        return qs
    
class RecipeListViewSearch(RecipeListViewBase):
    template_name = 'recipes/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q', '')

        if not search_term:
            raise Http404()
        
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term),
            )
        )
        return qs
    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')

        ctx.update({
            'page_title': f'Search for "{search_term}" |',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })
        return ctx

class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/pages/recipe-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'is_detail_page': True
        })
        return ctx
    

# def home(request):  # noqa: E302
#     recipes = Recipe.objects.filter(
#         is_published=True,
#     ).order_by('-id')

#     # messages.error(request, 'Epa, você foi pesquisar algo que eu vi.')
#     # messages.success(request, 'Epa, você foi pesquisar algo que eu vi.')
#     # messages.info(request, 'Epa, você foi pesquisar algo que eu vi.')

#     # current_page = request.GET.get('page', 1)
#     # try:
#     #     current_page = int(request.GET.get('page', 1))
#     # except ValueError:
#     #     current_page = 1
#     # paginator = Paginator(recipes, 9)
#     # page_obj = paginator.get_page(current_page)

#     # pagination_range = make_pagination_range(
#     #     paginator.page_range,
#     #     4,
#     #     current_page,
#     # )
#     page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

#     return render(request, 'recipes/pages/home.html', context={
#         'recipes': page_obj,
#         'pagination_range': pagination_range,
#     })


# def category(request, category_id):
#     recipes = get_list_or_404(
#         Recipe.objects.filter(
#             category__id=category_id,
#             is_published=True,
#         ).order_by('-id')
#     )

#     page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

#     return render(request, 'recipes/pages/category.html', context={
#         # 'recipes': recipes,
#         'recipes': page_obj,
#         'pagination_range': pagination_range,
#         'title': f'{recipes[0].category.name} - Category | '
#     })


# def recipe(request, id):
#     # recipe = Recipe.objects.filter(
#     #     pk=id,
#     #     is_published=True,
#     # ).order_by('-id').first()
#     recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

#     return render(request, 'recipes/pages/recipe-view.html', context={
#         'recipe': recipe,
#         'is_detail_page': True,
#     })


# def search(request):
#     search_term = request.GET.get('q', '').strip()  # strip >> função python para remover espaços

#     # caso procure vazio, levanta erro 404
#     if not search_term:
#         raise Http404()

#     # procurar entre os titulos OU descrições a palavra digitada no campo search
#     recipes = Recipe.objects.filter(
#         Q(
#             Q(title__icontains=search_term) |
#             Q(description__icontains=search_term),
#         ),
#         is_published=True
#     ).order_by('-id')

#     page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

#     return render(request, 'recipes/pages/search.html', {
#         'page_title': f'Search for "{search_term}" |',
#         'search_term': search_term,
#         # 'recipes': recipes,
#         'recipes': page_obj,
#         'pagination_range': pagination_range,
#         'additional_url_query': f'&q={search_term}',
#     })


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
