from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorsBaseTest

class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )
    
    def fill_form_dummy_data(self, form):

        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def test_empty_first_name_error_message(self):
        # Acessando página
        self.browser.get(self.live_server_url + '/authors/register/')
        # self.sleep(5)
        # Selecionando form principal do browser
        form = self.browser.find_element(
            By.XPATH,            
            '/html/body/main/div[2]/form'   # para pegar esse XPATH, clica em cima com botão direito sobre o código form que quer, e seleciona xpath em cópia
        )

        # Verificando se está ativo e incluindo email
        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        # selecionando input first-name, incluindo texto (espaços) para o form e clicando ENTER
        first_name_field = self.get_by_placeholder(form, 'Ex.: John')
        first_name_field.send_keys(' ')
        first_name_field.send_keys(Keys.ENTER)

        # Selecionando página novamente, após ENTER atualizar página, para fazer assertIn
        form = self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

        self.sleep(5)

        # Verificand se o texto abaixo tem no first_name
        self.assertIn('Write your first name', form.text)