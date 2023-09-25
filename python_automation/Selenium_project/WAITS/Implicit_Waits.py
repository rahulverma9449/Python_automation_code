from selenium import webdriver



driver = webdriver.Chrome(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')
driver.implicitly_wait(10)


driver.get('D:\Autodata\Autodata\Selenium_project\WAITS\sample.html')
my_image = driver.find_element('ID', 'languages lists')
my_image.click()
print("FOund image")