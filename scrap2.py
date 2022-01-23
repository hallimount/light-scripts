# Парсер ссылок на веб-странице по тэгу <a>
# HAVE TO DO:
# - Репорт в формате .csv, .html или JSON с отправкой на почту (smtplib), телеграм через api id пользователя (telethon)


from bs4 import BeautifulSoup as bsoup
import urllib
import urllib.parse
import urllib.request
from urllib.request import urlopen



url = input('URL ссылка (http(s)://domain)- ')
    print(url)
    r = requests.head(url)
    
    if r.status_code == 200:                         # Пингование
        
        message = url +"  returned  200"
        print(message)
    else:

        message =  url + "   not available at the moment"
        print(message)


html = urlopen(url).read()
soup = bsoup(html)

tags = soup('a')

for tag in tags:
    print (tag.get('href',None))
