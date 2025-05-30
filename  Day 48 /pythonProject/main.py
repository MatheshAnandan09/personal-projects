from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_option)
driver.get('https://www.python.org')

time = []
name = []

for i in range(1,6):
    date = driver.find_elements(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    dates = [i.text for i in date]
    time.append(dates)
    names = driver.find_elements(By.XPATH, value = f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    event = [i.text for i in names]
    name.append(event)

results = {}

for n in range(len(time)):
    result = {
        'time' : time[n],
        'name' : name[n]
    }
    results[n] = result

print(results)





driver.quit()
