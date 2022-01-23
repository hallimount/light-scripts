# Парсер заголовков страницы
# MUST do: 
# - Перестает работать на некоторых сайтах по данным тэгам. СРОЧНО пофиксить!!

import requests 
from bs4 import BeautifulSoup 
 
 

def main():
    url = ''                                  # !!!!!!!!! LINK !!!!!!!!!
    r = requests.get(url)
    with open('test.html', 'w', encoding='utf-8') as output_file:
        soup = BeautifulSoup(r.text, 'html.parser')
        for i in soup.select(".items > .article-summary > .article-description"):
            title = i.select(".caption > a[href]")
            output_file.writelines("<h2>" + title[0].text + "</h2>")
 
 
if __name__ == '__main__':
    main()