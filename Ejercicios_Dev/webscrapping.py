# generar script con selenium para consultar datos de la pagina de la bolsa de valores de chile

# Importar librerias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Inicializar el driver
driver = webdriver.Chrome(executable_path=r"C:\Users\camilo.gonzalez\Downloads\chromedriver.exe")

# Ingresar a la pagina
driver.get("https://www.bolsadesantiago.com/resumen_instrumento/LTM")

# Esperar 5 segundos
time.sleep(5)

# Obtener el valor de la accion
valor = driver.find_element("xpath","//h4 a[@class='text-muted ng-binding']").text

# Obtener el valor de la accion
valor = driver.find_element("xpath","//h4/a").text

print(valor)