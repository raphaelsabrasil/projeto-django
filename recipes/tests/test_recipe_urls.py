from django.test import TestCase
from django.urls import reverse

class RecipeURLsTests(TestCase):
    # def test_the_pytest_is_ok(self):
    #     # variavel = '123456'
    #     print('OLÁ MUNDO')
    #     assert 1 == 1, 'Um é igual a um'
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'pk': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
    
    # RED - GREEN - REFACTOR