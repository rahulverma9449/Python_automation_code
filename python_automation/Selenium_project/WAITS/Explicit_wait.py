from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.firefox(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')
 # driver.explicit_wait()

driver.get('http://demostore.supersqa.com/')
# my_image = driver.find_element('ID', 'languages lists')

my_image =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Languages lists')))

# if my_image.is_displayed():
#     print("Pass+")
print("Found image")

driver.find_element(By.CSS_SELECTOR, '#BMW').click()
series_6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth')))