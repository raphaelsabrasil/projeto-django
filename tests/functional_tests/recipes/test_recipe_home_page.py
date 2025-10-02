import pytest
from unittest.mock import patch
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test        # >>> para executar no terminal: pytest -m functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # def test_the_test(self):
    
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

    @patch('recipes.views.PER_PAGE', new=2)     # mostra quantidade de receitas por página
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()

        title_needed = 'This is what I need'

        recipes[0].title = title_needed         # colocando nome na primeira receita com esse título
        recipes[0].save()

        #Usuário abre a página
        self.browser.get(self.live_server_url)

        #Vê um campo de busca com o texto "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
        )

        #Clica neste input e digita o termo de busca para encontrar a receita com o título desejado
        # search_input.click()
        search_input.send_keys(title_needed)        # para mandar texto no search_input
        search_input.send_keys(Keys.ENTER)

        self.sleep()

        #O usuário vê o que estava procurando na página
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text,
        )

    @ patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_pagination(self):
        self.make_recipe_in_batch()

        #Usuário abre a página
        self.browser.get(self.live_server_url)

        #Vê que tem uma paginação e clica na página 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'   # Documentação Acessibilidade (ARIA) >>> https://developer.mozilla.org/pt-BR/docs/Web/Accessibility/ARIA
        )
        page2.click()

        self.sleep()

        #Vê que tem mais 2 receitas na página 2
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            2
        )



# para executar no terminal somente este teste: pytest -k test_recipe_home_page_without_recipes_not_found_message
