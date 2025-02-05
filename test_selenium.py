from selenium import webdriver

# Inicializa o ChromeDriver
driver = webdriver.Chrome()

# Acessa o Mercado Livre
driver.get("https://www.mercadolivre.com.br/")

print("Selenium funcionando!")

# Fecha o navegador
driver.quit()
