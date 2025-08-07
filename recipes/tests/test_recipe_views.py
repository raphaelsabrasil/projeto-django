#from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
#from recipes.models import Category, Recipe, User
from .test_recipe_base import RecipeTestBase, Recipe


class RecipeViewsTest(RecipeTestBase):
    # def tearDown(self) -> None:
    #     return super().tearDown()
    
    # SETUP
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)    
    # TEARDOWN

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(      # quer saber se 'no recipe found' está no código.
            '<h1>No recipes found here 🥲</h1>',        
            response.content.decode('utf-8')
        )

    # Fixtures
    def test_recipe_home_template_loads_recipes(self):               
        # Need a recipe for this test
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        # Check if one recipe exists
        self.assertIn('Recipe Title', content)
        # self.assertIn('Recipe Description', content)
        # self.assertIn('10 Minutos', content)
        # self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)      # quantidade de receitas
        


    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        