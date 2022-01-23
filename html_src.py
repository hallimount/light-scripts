# Исходник HTML страницы
import requests 
 
 
def main():

    url = input('URL - ')
    print(url)
    r = requests.head(url)
    
    if r.status_code == 200:                 # Ping
        
        message = url +"  Active"
        print(message)
    else:

        message =  url + "   not available at the moment"
        print(message)
        return

    # Получаем страницу
    g = requests.get(url)
    # Открываем файл
    with open('source_html.html', 'w', encoding='utf-8') as output_file:
        
        output_file.write(g.text)
 
 

if __name__ == '__main__':
    main()