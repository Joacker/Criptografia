#LIBRARIES
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#/usr/local/bin/chromedriver
driver_path = '/usr/local/bin/chromedriver'

def login():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.rebellion.es/tiendarebel/logintienda.php')
    time.sleep(5)
    username = driver.find_element_by_name('usuario')
    username.clear()
    time.sleep(1)
    username.send_keys("ChupeteSuazo")
    pwd = driver.find_element_by_name("clave")
    pwd.clear()
    pwd.send_keys('1234567')
    driver.find_element_by_class_name("botonformulario").submit()
    time.sleep(5)
    driver.get('https://www.rebellion.es/tiendarebel/logintienda.php?error=si')
    time.sleep(15)
    driver.quit()

if __name__ == "__main__":
    #Variables
    login()