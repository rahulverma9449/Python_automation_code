# https://developer.mozilla.org/en-US/docs/web/css/css_selectors
# https://www.w3schools.com/cssref/css_selectors.asp

# css selector best selector after ID
# fast for selenium next to ID
# easy to write
# better than xpath (even the u hear the word so much more)

# go to 'http://demostore.supersqa.com'

# ========================================
# Simply use id or class as css locator
#'.' is for class
# '#' is for ID
#site-navigation'

# Example find the nav bar
# css using id = #site-navigation
# css using id = nav#site-navigation
# css using class = .main-navigation
# css using class = nav.main-navigation

# Two ways to test selector on Chrome developer tools
# 1. Simply Search (cmd+f then nav#site-navigation)


###########any atribute ##########

#$$('[data-product_id="23"]')
# * contains word
# ^ start with word
# $ ends with word
# the following 4 css have same result ( the wildcard ones can have more matches)
# 'a[title="view your shopping cart"]'
# 'a[tile^='View your"]'
# 'a[title*="shopping"]'
# 'a[title$="cart"]'

######### exclude selector ###########

# $$('li.product:not(.product-type-variable)')
