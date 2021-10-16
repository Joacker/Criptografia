#LIBRARIES
import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#/usr/local/bin/chromedriver
driver_path = '/usr/local/bin/chromedriver'

if __name__ == "__main__":
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
    pwd.send_keys('123456')
    driver.find_element_by_class_name("botonformulario").submit()
    time.sleep(5)
    driver.get('https://www.rebellion.es/tiendarebel/logintienda.php?error=si')
    time.sleep(15)
    driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/table[2]/tbody/tr/td[2]/a').click()
    time.sleep(5)
    oldkey = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[12]/td[2]/input')
    oldkey.clear()
    oldkey.send_keys('123456')
    time.sleep(2)
    newkey = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[13]/td[2]/input')
    newkey.clear()
    newkey.send_keys('1234567')
    time.sleep(2)
    rnewkey = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[14]/td[2]/input')
    rnewkey.clear()
    rnewkey.send_keys('1234567')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/input[1]').submit()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/input[14]').submit()
    time.sleep(6)
    driver.quit()

