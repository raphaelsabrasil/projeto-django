from django.contrib import admin

# Register your models here.
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...



# @admin.register  <<< também pode usar decorator ao invés de 'admin.site.register'