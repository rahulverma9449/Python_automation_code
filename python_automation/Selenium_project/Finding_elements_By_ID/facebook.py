from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options

# usr = input('Enter Email Id:')
# pwd = input('Enter Password:')

driver = webdriver.Firefox()
driver.get('https://www.flipkart.com/')
print("Opened flipkart")
sleep(1)


try:
    driver.find_element_by_xpath('//body[@class="_2KpZ61 _2doB4z"]').click()

except:
    pass

username_box = driver.find_element_by_id('email').send_keys(7834932769)
print("Email Id entered")
sleep(1)

# password_box = driver.find_element_by_id('pass')
# password_box.send_keys(pwd)
# print("Password entered")

login_box = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input ' )
login_box.click()

print("Done")
print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")