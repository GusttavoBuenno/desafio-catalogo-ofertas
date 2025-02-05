from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time
import undetected_chromedriver as uc

# Configuração do Chrome em modo headless (sem interface gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")  

# Inicializando o driver com undetected_chromedriver
service = Service(ChromeDriverManager().install())
driver = uc.Chrome(service=service, options=chrome_options)

URL = "https://www.mercadolivre.com.br/ofertas#nav-header"

def buscar_produtos():
    driver.get(URL)

    try:
        # Aguardar um elemento chave para garantir que a página carregou (mude o XPATH conforme necessário)
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Ofertas")]'))
        )
    except TimeoutException as e:
        print(f"Erro de timeout ao carregar a página: {e}")
        return []
    except Exception as e:
        print(f"Erro ao carregar a página: {e}")
        return []

    # Rolar até o final da página para garantir que o conteúdo seja carregado
    for i in range(3):  # Rolar 3 vezes
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Aguarda 3 segundos após rolar

    # Verificar o código-fonte da página para depurar
    page_source = driver.page_source
    print(page_source)  # Imprime o código-fonte da página para análise

    produtos = []

    # Ajuste o XPATH caso necessário (verifique o conteúdo real da página)
    itens = driver.find_elements(By.XPATH, '//li[contains(@class, "promotion-item")]')
    if not itens:
        print("Nenhum item encontrado com o XPATH fornecido.")
    else:
        print(f"Itens encontrados: {len(itens)}")

    for item in itens[:10]:  # Limitar a 10 produtos
        try:
            nome = item.find_element(By.XPATH, './/p[@class="promotion-item__title"]').text
            preco = item.find_element(By.XPATH, './/span[@class="andes-money-amount__fraction"]').text
            link = item.find_element(By.XPATH, './/a').get_attribute("href")

            produto = {
                "nome": nome,
                "preco": preco,
                "link": link
            }
            produtos.append(produto)
        except Exception as e:
            print(f"Erro ao processar produto: {e}")

    return produtos

if __name__ == "__main__":
    try:
        resultados = buscar_produtos()

        if resultados:
            for produto in resultados:
                print(produto)
        else:
            print("Nenhum produto encontrado.")

    finally:
        try:
            driver.quit()  # Garante que o driver será fechado corretamente
        except Exception as e:
            print(f"Erro ao fechar o driver: {e}")
