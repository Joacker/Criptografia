#LIBRARIES
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
    driver.get('https://www.rebellion.es/tiendarebel/registrate.php')
    time.sleep(5)
    nombre = driver.find_element_by_name('Nombre')
    nombre.clear()
    time.sleep(1)
    nombre.send_keys('Humberto')
    apellido1 = driver.find_element_by_name('Apellido1')
    apellido1.clear()
    apellido1.send_keys("Suazo")
    apellido2 = driver.find_element_by_name('Apellido2')
    apellido2.clear()
    apellido2.send_keys('Pontivo')
    #provincia = driver.find_element_by_name('Provincia')
    pais = Select(driver.find_element_by_name('Pais'))
    pais.select_by_visible_text('Chile')
    direccion = driver.find_element_by_name('Direccion')
    direccion.clear()
    direccion.send_keys('CALLE PORTAL DE GAMARRA, 48 - 01013 - VITORIA-GASTEIZ (ALAVA)')
    '''cp = driver.find_element_by_name('CodigoPostal')
    cp.clear()
    cp.send_keys('01006')
    poblacion = driver.find_element_by_name('Poblacion')
    poblacion.clear()
    poblacion.send_keys('5')
    provincia = Select(driver.find_element_by_name('Provincia'))
    provincia.select_by_visible_text('Alava')'''
    telefono = driver.find_element_by_name('Telefono')
    telefono.clear()
    telefono.send_keys('962923531')
    email = driver.find_element_by_name('email')
    email.clear()
    email.send_keys('cucadaxu@acrossgracealley.com')
    usuario = driver.find_element_by_name('Usuario')
    usuario.clear()
    usuario.send_keys('Ben10Brereton')
    clave = driver.find_element_by_name('Clave')
    clave.clear()
    clave.send_keys('123456')
    clave2 = driver.find_element_by_name('Clave2')
    clave2.clear()
    clave2.send_keys('123456')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/input[1]').click()
    time.sleep(8)
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form/input[13]').click()
    time.sleep(5)
    driver.close()