from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://facebook.com")

#driver.get("https://github.com/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "email").send_keys("rahulkumar9449@gmail.com")
# find password input field and insert password as well
driver.find_element("id", "pass").send_keys('Rahul@123')
# click login button
driver.find_element("name", "login").click()