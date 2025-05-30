import smtplib

from bs4 import BeautifulSoup
import requests
import os
from smtplib import SMTP
my_email = os.environ.get('MAIL_ID')
password = os.environ.get('PASSWORD')

headers = {
    "Host": "myhttpheader.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "sec-fetch-site": "none",
    "Accept-Encoding": "gzip, deflate",
    "upgrade-insecure-requests": "1",
    "sec-fetch-mode": "navigate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
    "sec-fetch-dest": "document",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "106.198.90.174"
}

URL = 'https://appbrewery.github.io/instant_pot/'
response=  requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price_ = soup.find(name = 'span', class_ ='a-price-whole')
after_point = soup.find(name = 'span', class_ = 'a-price-fraction')
price = float(price_ +after_point)

if price <100:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg= f'Price Drop alert\n\nThe price has droped.Current price {price}')



