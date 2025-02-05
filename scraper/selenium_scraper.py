from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def coletar_produtos():
    # Configuração do Selenium
    options = Options()
    options.headless = True  # Executar sem abrir o navegador
    driver = webdriver.Chrome(options=options)

    # Acessar o Mercado Livre
    driver.get("https://www.mercadolivre.com.br/ofertas?as_word=Computador%20Gamer%20i7%2016gb%20ssd%201tb")

    produtos = []

    # Encontrar os elementos da página com os dados dos produtos
    itens = driver.find_elements(By.CLASS_NAME, 'ui-search-result')

    for item in itens:
        try:
            nome = item.find_element(By.CLASS_NAME, 'ui-search-item__title').text
            preco = item.find_element(By.CLASS_NAME, 'price__fraction').text
            preco_sem_desconto = item.find_element(By.CLASS_NAME, 'price__discount').text if item.find_elements(By.CLASS_NAME, 'price__discount') else None
            imagem = item.find_element(By.CLASS_NAME, 'ui-search-result-image__element').get_attribute("src")
            link = item.find_element(By.CLASS_NAME, 'ui-search-item__link').get_attribute("href")
            parcelamento = item.find_element(By.CLASS_NAME, 'ui-search-price__part').text if item.find_elements(By.CLASS_NAME, 'ui-search-price__part') else None
            tipo_entrega = item.find_element(By.CLASS_NAME, 'ui-search-item__shipping').text if item.find_elements(By.CLASS_NAME, 'ui-search-item__shipping') else 'Normal'
            frete_gratis = 'Frete grátis' in tipo_entrega

            # Percentual de Desconto
            percentual_desconto = None
            if preco_sem_desconto:
                preco_sem_desconto = preco_sem_desconto.replace('R$', '').strip()
                preco = preco.replace('R$', '').strip()
                percentual_desconto = (float(preco_sem_desconto.replace('.', '').replace(',', '.')) - float(preco.replace('.', '').replace(',', '.'))) / float(preco_sem_desconto.replace('.', '').replace(',', '.')) * 100

            produto = {
                'nome': nome,
                'preco': preco,
                'preco_sem_desconto': preco_sem_desconto,
                'imagem': imagem,
                'link': link,
                'parcelamento': parcelamento,
                'percentual_desconto': percentual_desconto,
                'tipo_entrega': tipo_entrega,
                'frete_gratis': frete_gratis
            }

            produtos.append(produto)
        except Exception as e:
            print(f"Erro ao coletar produto: {e}")

    driver.quit()
    return produtos
