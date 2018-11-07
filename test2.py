from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import logging

#launch url
url = "https://declaraciones.sri.gob.ec/tuportal-internet/"

# create a new Chrome session
driver = webdriver.Chrome()
#driver.implicitly_wait(30)
driver.get(url)

element = driver.find_element_by_id("userPri")
element.send_keys("")

element = driver.find_element_by_id("password-2")
element.send_keys("")

python_button = driver.find_element_by_name("boton")
python_button.click()

python_button = driver.find_element_by_xpath("//button[@title='ocultar']")
python_button.click()

declaraciones = driver.find_element_by_xpath("//a[@id='sri-menu-icon-declaraciones']")
declaraciones.click() 

consultas = driver.find_element_by_xpath("//a[@id='Consultas']")
consultas.click() 

declaracionesInternet = driver.find_element_by_xpath("//a[@href='https://declaraciones.sri.gob.ec/tuportal-internet/menusFavoritos.jspa?redireccion=77&idGrupo=76']")
declaracionesInternet.click() 




