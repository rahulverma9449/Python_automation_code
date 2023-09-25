# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import selenium.webdriver.common.by
# ##driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')
driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(3)