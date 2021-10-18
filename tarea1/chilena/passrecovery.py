#LIBRARIES
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#/usr/local/bin/chromedriver
driver_path = '/usr/local/bin/chromedriver'

if __name__ == '__main__': 
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    #Iniciar interfaz 
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://www.entrejuegos.cl/recuperar-contrase%C3%B1a')
    time.sleep(3)
    email = driver.find_element_by_name('email')
    email.clear()
    time.sleep(1)
    email.send_keys('jfernandezvizcarra@gmail.com')
    time.sleep(5)
    driver.find_element_by_name('submit').click()
    time.sleep(8)
    driver.close()