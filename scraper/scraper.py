from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .models import Produto
from bs4 import BeautifulSoup

import time

def coletar_produtos():
    # Configura o WebDriver do Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Roda em segundo plano, sem abrir o navegador
    service = Service("./scraper/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Acesse a página
    driver.get("https://mercadolivre.com.br")


    # Aguarde a página carregar (ajuste o tempo se necessário)
    time.sleep(5)  # Aumente se necessário para a página carregar

    # Extraia o HTML da página após o carregamento do JavaScript
    html = driver.page_source
    driver.quit()

    # Analise o HTML com BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Exemplo de como buscar produtos com Selenium/BeautifulSoup
    produtos = []
    for item in soup.find_all("li", class_="ui-search-layout__item"):  # Verifique a classe correta
        nome = item.find("h2", class_="ui-search-item__title")
        preco = item.find("span", class_="price")
        link = item.find("a", class_="ui-search-link")

        if nome and preco and link:
            produto = Produto(
                nome=nome.text.strip(),
                preco=preco.text.strip(),
                link=link.get("href")
            )
            produtos.append(produto)

    # Salva os produtos no banco de dados
    Produto.objects.bulk_create(produtos)

    if not produtos:
        print("Nenhum produto encontrado.")
    return produtos
