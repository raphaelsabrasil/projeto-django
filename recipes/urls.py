from django.urls import path
#from recipes.views import home
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewCategory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),    
]

# path('', views.home, name="recipes-home") <<< usado caso não defina um app_name