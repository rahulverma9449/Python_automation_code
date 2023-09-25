from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

url = 'D:\python network\Autodata\python_automation\Selenium_project\Sending_keys\Drop_down1.html'

driver.get(url)

mu_dropdown = driver.find_element(('class', '.dropbtn'))

import pdb; pdb.set_trace()