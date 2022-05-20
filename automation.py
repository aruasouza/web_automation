from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')
def barra_busca():
    return navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
barra_busca().send_keys('dólar hoje')
barra_busca().send_keys(Keys.ENTER)
def cotacao():
    return navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
dolar = cotacao().get_attribute('data-value')
print(dolar)
navegador.get('https://www.google.com.br/')
barra_busca().send_keys('euro hoje')
barra_busca().send_keys(Keys.ENTER)

euro = cotacao().get_attribute('data-value')
print(euro)