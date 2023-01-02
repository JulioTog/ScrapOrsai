#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import winsound
import time

geckodriver = 'geckodriver.exe'
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.headless = True
browser = webdriver.Firefox(executable_path=geckodriver, options=options)
url = "https://suscripcion.orsai.org/"
browser.get(url)
delay = 10
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME , "bg-blue-500"))
    )      
    html = browser.page_source
    soup = BeautifulSoup(html)
    div = soup.div.div.div
    text = div.find('div','text-sm mt-4').get_text()
    monto = div.find('div','text-2xl').get_text()

    cantidad = re.search(r'\d+',text).group(0)
    print(cantidad)
    f = open("resutlt.txt","a")
    f.write(cantidad + " ---> " + monto + " ---> " + time.asctime( time.localtime(time.time()) ) +"\n")
    if int(cantidad) < 100 :
        winsound.PlaySound('test.wav', winsound.SND_FILENAME)
finally:
    print("QUIT")
    
    browser.quit()



