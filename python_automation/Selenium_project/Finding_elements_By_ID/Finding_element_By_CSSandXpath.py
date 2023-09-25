from selenium import webdriver
from selenium.webdriver.common.by import By
import time




driver = webdriver.Firefox()

driver.get('https://www.flipkart.com')

time.sleep(5000)
driver.find_element_by_xpath()



element =  driver.find_element()

cart = driver.find_element(By.CSS_SELECTOR, "#site-header-cart")
time.sleep(3)
cart.click()

# Click my account

cart = driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a")
time.sleep(3)
cart.click()

# Click By XPATH

xpath_1 = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[3]/a')
time.sleep(3)
xpath_1.click()


xpath_1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
time.sleep(3)
xpath_1.click()



# time.sleep(3)
# driver.quit()
