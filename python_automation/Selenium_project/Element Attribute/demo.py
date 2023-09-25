from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



serve = Service("D:\\Autodata\\Autodata\\chromedriver.exe")
#driver = webdriver.firefox(executable_path="D:\\Autodata\\Full_stack_developer\\geckodriver.exe")
driver = webdriver.Chrome(service=serve)
#webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com")
mypagetitle = driver.title
print(mypagetitle)
