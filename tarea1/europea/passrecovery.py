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
    driver.get('https://www.rebellion.es/tiendarebel/recordarcontrasena.php')
    time.sleep(3)
    username = driver.find_element_by_name('usuario')
    username.clear()
    time.sleep(1)
    username.send_keys('ChupeteSuazo')
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[8]/td/input[2]').submit()
    time.sleep(8)
    driver.close()