from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = 'balaanand727@gmail.com'
ACCOUNT_PASSWORD = 'mathesh100daysofcode'
PHONE = '6379841562'

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4002677241&f_LF=f_AL&geoId=106888327&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true")

sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()

time.sleep(2)

name = driver.find_element(By.XPATH, value= '//*[@id="base-sign-in-modal_session_key"]')
name.send_keys(ACCOUNT_EMAIL)
print('Name has been entered')

time.sleep(2)

password = driver.find_element(By.XPATH, value = '//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(ACCOUNT_PASSWORD)
print('Password has been enteres')

time.sleep(2)

acc_sign_in = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
acc_sign_in.click()
print('Signed In')
time.sleep(25)

# all_jobs = WebDriverWait(driver, 30).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.jobs-search-results__list-item'))
# )
#
# # Loop through each job element and print its text
# for job in all_jobs:
apply = driver.find_element(By.XPATH, value = '//*[@id="ember53"]')
apply.click()

time.sleep(2)

phone = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4002677241-8878800100-phoneNumber-nationalNumber"]')
phone.send_keys(PHONE)

time.sleep(2)

next_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary')
next_button.click()

