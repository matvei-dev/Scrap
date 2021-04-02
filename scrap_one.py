from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://fenglish.ru/films')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('h6')
for name in nameList:
    print(name.get_text().strip())
