from pathlib import Path
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

# print(ROOT_PATH)
# print(CHROMEDRIVER_PATH)

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    # >>> código abaixo para ignorar logs de erro:     
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
    
    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':    
    browser = make_chrome_browser()
    browser.get('http://udemy.com/')
    sleep(5)
    browser.quit()



    # >>> código abaixo para criar lista de opções a serem passadas ao navegador, para silenciar logs e evitar o erro "PHONE_REGISTRATION_ERROR"
    # options_to_add = [
    #     '--headless',     <<< faz com que o navegador rode em segundo plano, sem interface gráfica. Não aparece nada.
    #     '--disable-extensions',
    #     '--log-level=3'
    # ]
    # # browser = make_chrome_browser('--headless')
    # browser = make_chrome_browser(*options_to_add)


# bin/chromedriver --help  <<< no terminal