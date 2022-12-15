from bs4 import BeautifulSoup
import urllib.request
from operator import itemgetter

req = urllib.request.urlopen('https://www.interfax.ru')
html = req.read()
soup = BeautifulSoup(html, 'html.parser')

# Создаю массивы для дальнейшей записи в них данных с новостей
newТews = []
maiNews = []

# Функция для записи главных новостей в массив maiNews
def writeMainNews(soupHTML):
    maiNewsSoup = soupHTML.find_all('div',class_='newsmain')
    maiNewsSoupA = maiNewsSoup[0].find_all('a')
    for item in maiNewsSoupA: 
        title = item.find('h3').get_text()
        href = item.get('href')
        maiNews.append({
            'title': title,
            'href': href
        })


# Функция для записи новых новостей в массив newТews
def writeNewNews(soupHTML):
    grupNewsSoup = soupHTML.find_all('div',class_='timeline__group')
    oneNewsSoup = soupHTML.find_all('div',class_='timeline__text')
    imgNewsSoup = soupHTML.find_all('div',class_='timeline__photo')
    grupNewsSoupDiv = []
    
    # Достаю новости из групп
    for item in grupNewsSoup:
        divs = item.find_all('div')
        for div in divs:
           grupNewsSoupDiv.append(div)
    
    grupNewsSoupDiv = grupNewsSoupDiv + imgNewsSoup + oneNewsSoup 
        
        
    for item in grupNewsSoupDiv: 
        title = item.find('h3').get_text()
        href = item.a.get('href')
        number = item.get('data-vr-contentbox')[5:]
        time = item.find('time').get_text()
        newТews.append({
            'title': title,
            'href': href,
            'time': time,
            'number': number
        })


def writeNewsFile(new, main):
    new.sort(key=itemgetter('number'))
    new.reverse ()
    file = open('news.txt', 'w', encoding='utf-8')
    
    numberMainNews = 1 
    file.write('Главыне новости')
    for news in main:
        file.write(f'\n\n Новость № {numberMainNews}\n\n\tНазвание: {news["title"]} \n\tСсылка: {news["href"]}\n\n ********************************\n ')
        numberMainNews += 1

    numberNewNews = 1
    file.write('\n\nНовые новости')
    for item in new:
        file.write(f'\n\n Новость № {numberNewNews}\n\nВремя: {item["time"]}  \n\tНазвание: {item["title"]} \n\tСсылка: {item["href"]}\n\n ********************************\n ')
        numberNewNews += 1
    
    file.close()


writeMainNews(soup)
writeNewNews(soup)
writeNewsFile(newТews, maiNews)