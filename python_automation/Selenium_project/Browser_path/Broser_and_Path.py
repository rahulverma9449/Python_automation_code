


from selenium import webdriver
from selenium.webdriver.chrome.service import  Service

website = "https://www.thesun.co.uk/sport/football/"
path = 'D:\\Autodata\\Autodata\\chromedriver.exe'

#driver = webdriver.Chrome(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
#

Containers = driver.find_element(by="xpath", value='//div[@class="teaser__copy-container"]')

# import webdriver_manager.drivers.chrome

# Option 2 is adding the executable to system path

# //div[@class="teaser__copy-container"]/a/h2

for container in Containers:
    container.find_element(by="xpath", value='./a/h2')
    container.find_element(by="xpath", value='./a/p')

# driver = webdriver.chrome()