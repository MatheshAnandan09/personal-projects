import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(url = zillow_url)

soup = BeautifulSoup(response.text, 'html.parser')


price = soup.find_all(name='span', class_ = 'PropertyCardWrapper__StyledPriceLine')
house_price = []
for i in price:
    prices =  i.text.split('/mo')[0].split('+')[0]
    house_price.append(prices)


address = soup.find_all('address', {'data-test': 'property-card-addr'})
house_address = []
for i in address:
    add = i.text.strip()
    house_address.append(add)

link = soup.find_all('div', class_ ='StyledPropertyCardPhotoBody')
house_link = []
for i in link:
    a =i.find('a')
    links = a.get('href')
    house_link.append(links)


print(f'Price:\n {house_price}')
print(f'Address:\n{house_address}')
print(f'Links:\n{house_link}')


for i in range(len(house_price)):

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdX3iCNh1ehxzlzIARqPfw3Q8WtNWlUr7TEAt769v_AoFKbxg/viewform')
    time.sleep(10)

    address_qn = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    address_qn.send_keys(house_address[i])
    time.sleep(3)
    price_qn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_qn.send_keys(house_price[i])
    time.sleep(3)
    link_qn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_qn.send_keys(house_link[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    driver.quit()

