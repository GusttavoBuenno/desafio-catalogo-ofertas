from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time


chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")  


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = "https://www.mercadolivre.com.br/ofertas#nav-header"

def buscar_produtos():
    driver.get(URL)

    try:
     
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@class="promotion-item"]'))
        )
    except TimeoutException as e:
        print(f"Erro de timeout ao carregar a página: {e}")
        return []
    except Exception as e:
        print(f"Erro ao carregar a página: {e}")
        return []

 
    time.sleep(5)  

    produtos = []

    
    itens = driver.find_elements(By.XPATH, '//li[@class="promotion-item"]')
    print(f"Itens encontrados: {len(itens)}")  

    for item in itens[:10]:  
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
    resultados = buscar_produtos()

    for produto in resultados:
        print(produto)

    driver.quit()
