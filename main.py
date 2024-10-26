from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций Chrome
chrome_options = webdriver.ChromeOptions()

# Установка и настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открытие веб-страницы
driver.get("http://www.google.com")

# Закрытие браузера
driver.quit()
