from selenium import webdriver
from selenium.webdriver.chrome.service import  Service

import time
driver = webdriver.Chrome(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')
driver.implicitly_wait(5)
# driver = webdriver.Chrome(driver=driver)
# driver.maximize_window()

# Get to Url
driver.get("https://google.com/")
time.sleep(1)

# Click on 'My Account' tab
my_acct_tab = driver.find_element_by_link_text("My account")
my_acct_tab.click()
time.sleep(3)




# scrole the page up
driver.execute_script("window.scrollBy(0,300")

# find username fild and input username
u_name_field = driver.find_element_by_id("username")
u_name_field.send_keys("rahulverma9449@gmail.com")

# find password field and input username
p_field = driver.find_element_by_id("password")
p_field.send_keys("Rahul@123")

# Click Login button
login_btn = driver.find_elements_by_name('Log in')
login_btn.click()
time.sleep(3)

# get displayed error

errors_list_elm = driver.find_element_by_name('ul.woocommerce-error li')
first_error_elm = errors_list_elm[0]
displayed_error_text = first_error_elm.text

# Verify the displayed error is as expected
expected_error = "ERROR: Invalid username.Lost your password?"
assert expected_error == displayed_error_text, "Displayed error is not as expected."
print("Success.")

# Close the browser
driver.quit()
