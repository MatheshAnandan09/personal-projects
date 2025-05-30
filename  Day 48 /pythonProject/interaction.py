from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_option)
driver.get('http://secure-retreat-92358.herokuapp.com')

# number = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#
# portal = driver.find_element(By.LINK_TEXT, value='Over My Dead Body')
# # portal.click()
# # driver.quit()
#
# search = driver.find_element(By.NAME, value = 'search')
# search.send_keys('tamil')
# search.send_keys(Keys.ENTER)
first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
sign_up = driver.find_element(By.XPATH, value='/html/body/form/button')

first_name.send_keys('Mathesh')
last_name.send_keys('Anandan')
email.send_keys('yoursu@gmail.com')
sign_up.send_keys(Keys.ENTER)

