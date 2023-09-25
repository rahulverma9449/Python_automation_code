from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('https://www.amazon.com')


cart_elm = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart_elm.text)

account_elm = driver.find_element(By.LINK_TEXT, 'My account')
print(account_elm.text)

account_elm_p = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(account_elm_p.text)

footer_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(footer_link.text)

# must be <a> tag or it will fail
tag = driver.find_element(By.LINK_TEXT, '0 items')
print(tag.text)

