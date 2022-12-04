from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

results = []

for item in news:
    title = item.find('span', class_='fz-16 fw-500 d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop fz-12').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })    
    
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание:{item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n*************************\n\n')
    i += 1

print(results, sep='\n')