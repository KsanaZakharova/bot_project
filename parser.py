'''

Parser

'''
# импортируем необходимые библиотеки BeautifulSoup4 и requests
from bs4 import BeautifulSoup as BS
import requests

# создаём переменную с сылкой сайта, к-го будем парсить
base_url = 'https://www.iamcook.ru/'
# Создаём словарь(наш индитификатор) , найти на сайте( Для разработчиков/Сеть/XHR/ id/ Заголовки /user-agent + accept
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/112.0.0.0 YaBrowser/23.5.1.721 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}

menu_day = ['Завтрак', 'Обед', 'Ужин']
def parser(url):
    session = requests.Session()
    response =session.get(url, headers=HEADERS) #   print(response.content) # выводит код страницы сплошным текстом
    soup = BS(response.content, "html.parser") # print(soup)# распарсим - выводим  уже дерево элементов
    items = soup.find_all('div',class_ ='open') # див - весь контент, класс - *по времени дня* / на странице сайта/ в исходном кода class=

# достаем название из класса
    for recipe in items:
        header = recipe.find('a',class_ ='menuheader').text
        recipe_events = [] # создаём пустой список, в к-й будем переносить данные
        if header in menu_day:
            events = recipe.find_all('li')
            events_str = header + events[0].text.rstrip() + events[1].text + '\n'
            recipe_events += events_str
        return recipe_events

parser(url=base_url)
