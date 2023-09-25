#By.ID,By.CSS_Selector, By.XPATH, By.Class_Name
#By.Link_Text, By.Partial_Link_Text
# By.Name, By.Tag_Name

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')
driver.get('http://demostore.supersqa.com')


cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()
# cart = driver.find_element(By.ID, '')

driver.get('http://demostore.supersqa.com/my-account/')
u_name = driver.find_element(By.ID, "username")
u_name.send_keys('rahulverma9449@gmail.com')
pdb.set_trace()


# NOTE: To find available methods just do dir(<variable>)

