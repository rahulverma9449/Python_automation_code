import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get('http://demostore.supersqa.com/my-account/')
# u_name = driver.find_element('id', 'username')
# u_name.send_keys("rahulverma9449@gmail.com")
#
# p_field = driver.find_element('id', 'password')
# p_field.send_keys('Rahul@123')
#
# submit_btn = driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
# submit_btn.click()
# Negative Test cases
search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
search_field.send_keys('lower')
time.sleep(3)
search_field.send_keys(Keys.ENTER)
