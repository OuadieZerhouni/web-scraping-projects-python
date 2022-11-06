from unicodedata import name
from webbrowser import get
import bs4 as bs
import requests
from time import sleep

n = 1

def scrap(url):
    global n
    html = requests.get(url).text
    soup = bs.BeautifulSoup(html, 'lxml')

    links = soup.find_all('a')
    text = soup.find('pre').text
    tables = text.split('\n')
    titles = []

    def replaceSpace(str) :
        return str.replace("%2", "")

    for table in tables:
        table = ' '.join(table.split())
        titles.append(table.split())

    with open('pdf-lib2.csv', 'a') as f:
        for i in range(1, len(links)):
            type = url[19:-1]

            if (links[i].get('href').endswith('.pdf') or links[i].get('href').endswith('.PDF') or links[i].get('href').endswith('.doc')):

                details = ''
                for j in range(0,len(titles[i])):
                    titles[i][j]=titles[i][j].replace(',','-')
                    details=details+titles[i][j]

                try:
                    type="forDummy"
                    f.write(str(n)+' ,' + type +' , '+url +
                            links[i].get('href')+' , '+ details + '\n')
                    n += 1
                except UnicodeEncodeError:
                    print(i)
                    pass
            elif (links[i].get('href').endswith('/')):
                sleep(1)
                scrap(url + links[i].get('href'))

                print(i, links[i].get('href'))

        print('pdfs=====>  : ', n)


scrap('https://the-eye.eu/public/Books/World%20Tracker%20Library/worldtracker.org/media/library/How-To/For%20Dummies%20eBook%20Collection/')


