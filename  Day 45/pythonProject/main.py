from bs4 import BeautifulSoup
import requests


responses = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

content = responses.text
soup = BeautifulSoup(content, 'html.parser')

title_card = soup.find_all(name = 'h3', class_ = 'title')
titles = [i.text for i in title_card]
titles.reverse()
with open('movies.txt', 'w') as file:
    file.writelines(f'{i}\n'for i in titles)



