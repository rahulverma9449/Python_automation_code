from selenium import webdriver
import pdb;

driver =webdriver.firefox(executable_path='D:\\Autodata\\Autodata\\chromedriver.exe')

driver.get('http://demostore.supersqa.com')


search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
place_holder = search_field.get_attribute('placeholder')
if place_holder != 'Search products…':
        raise Exception("Place holder for search field is not as expected. Actual:{}".format(place_holder))
else:
    print("PASS")

# Example 12
# my_accnt = driver.find_element('css selector', 'li.page-item-9')
# my_accnt.click()
#
# nav_items = driver.find_elements('css selector', 'ul.nav-menu li')
#
# for item in nav_items:
#     item_class = item.get_attribute('class')
#     if 'current_page_item' in item_class:
#         print("The selected tab is: {}".format(item.text))


# Example (get url link)

product_link = driver.find_element('scc selector', 'li.product a')
product_url = product_link.get_attribute('href')
print("The url for product is : {}".format(product_url))

pdb.set_trace()

