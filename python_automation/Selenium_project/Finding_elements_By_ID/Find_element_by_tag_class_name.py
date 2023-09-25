
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.firefox(executable_path='D:\\Autodata\\Autodata\\geckodriver.exe')

driver.get("http://www.google.com/")

# Examples is finding by class name

product = driver.find_element(By.CLASS_NAME, 'product')
product = driver.find_element(By.CLASS_NAME, 'product')
# print(product)
# print("=================")
# print(product)

# Example of finding by 'name'
orderby = driver.find_element(By.NAME, 'orderby')
print(orderby.text)

# example of finding by 'TAG'

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Found number of 'a' tag: {len(all_links)}")


all_list = driver.find_elements(By.TAG_NAME, 'li')
print(f"Found number of 'li' tag: {len(all_list)}")

