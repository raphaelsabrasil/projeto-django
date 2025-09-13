from selenium.webdriver.common.by import By
import pytest

from base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    # def test_the_test(self):
    def test_recipe_home_page_without_recipes_not_found_message(self):        
        # browser = make_chrome_browser()   <<< não precisa, pois já está sendo executado por 'def setUp'
        self.browser.get(self.live_server_url)
        # self.sleep(6) <<< não precisa, pois já tem a def 'sleep'
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here 🥲', body.text)
        # browser.quit()    <<< não precisa, pois já está sendo executado por 'def tearDown'