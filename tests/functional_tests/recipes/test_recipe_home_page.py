from unittest.mock import patch
from selenium.webdriver.common.by import By
import pytest

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test        # >>> para executar no terminal: pytest -m functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # def test_the_test(self):
    @patch('recipes.views.PER_PAGE', new=2)     # mostra quantidade de receitas por página
    def test_recipe_home_page_without_recipes_not_found_message(self):        
        # browser = make_chrome_browser()   <<< não precisa, pois já está sendo executado por 'def setUp'
        # self.make_recipe()      # usado com mixin de class RecipeMixin(), para criar receita para o teste 
        # self.make_recipe_in_batch(qtd=20)       # mostra quantas receitas foram criadas
        self.browser.get(self.live_server_url)
        # self.sleep(6) <<< não precisa, pois já tem a def 'sleep'
        body = self.browser.find_element(By.TAG_NAME, 'body')
        # self.sleep()            # usado para dar tempo ao abrir o browser, vindo de método sleep, da class do módulo .base
        self.assertIn('No recipes found here 🥲', body.text)
        # browser.quit()    <<< não precisa, pois já está sendo executado por 'def tearDown'

    # para executar no terminal somente este teste: pytest -k test_recipe_home_page_without_recipes_not_found_message
