import requests
from bs4 import BeautifulSoup as BS


url = "https://habr.com/ru/articles/top/weekly/"


r = requests.get(url)
soup = BS(r.text, 'html.parser')
h2_tegs = soup.find_all('h2')


for h2 in h2_tegs:
    a = h2.find('a')
    if a:
        art_url = a.get('href')

        #оно жаловолось на неполную ссылку так что это исправление
        if not art_url.startswith('http'):
            art_url = 'https://habr.com' + art_url


        art_numb = art_url.split('/')[-2]


        art_r = requests.get(art_url)


        with open(f'{art_numb}.html', 'w', encoding='utf-8') as file:
            file.write(art_r.text)
    else:
        print('Сохранение...')