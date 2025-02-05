from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def obter_produtos():
    # Configuração do Selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Acesse o site de produtos (exemplo)
    driver.get("https://www.mercadolivre.com.br")
    time.sleep(2)  # Espera a página carregar

    produtos = []

    # Localiza os produtos na página (exemplo de estrutura)
    itens = driver.find_elements(By.CLASS_NAME, 'ui-search-result__content')
    
    for item in itens:
        nome = item.find_element(By.CLASS_NAME, 'ui-search-item__title').text
        preco = item.find_element(By.CLASS_NAME, 'price-tag-fraction').text
        descricao = item.find_element(By.CLASS_NAME, 'ui-search-item__group__element').text

        produtos.append({
            'nome': nome,
            'preco': preco,
            'descricao': descricao
        })
    
    driver.quit()
    
    return produtos
