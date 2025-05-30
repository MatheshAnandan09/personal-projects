from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_option)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

powers = driver.find_elements(By.CSS_SELECTOR, value='#store div')
power_id = [power.get_attribute('id') for power in powers]
cookie = driver.find_element(by=By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

is_game_on = True
while is_game_on:
    cookie.click()
    if timeout > five_min:
        prices = driver.find_elements(By.CSS_SELECTOR, value= '#store b')
        all_price =[]
        for i in prices:
            element_text = i.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                all_price.append(cost)
        customer_dic = {}
        for n in range(len(all_price)):
            customer_dic[all_price[n]] = power_id[n]
        money_element = driver.find_element(By.ID, value='money').text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        affordable_upgrades = {}
        for cost, id in customer_dic.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
                # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        is_game_on = False








