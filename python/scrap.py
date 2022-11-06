#import bs4 and request modules
from webbrowser import get
import bs4 as bs
import requests 
import sqlite3


url = 'https://the-eye.eu/public/Books/World%20Tracker%20Library/worldtracker.org/media/library/Mathematics/Calculus/' #'https://the-eye.eu/public/3D/Thingiverse/'
html = requests.get(url).text
soup = bs.BeautifulSoup(html, 'lxml')


links = soup.find_all('a')

text = soup.find('pre').text
tables= text.split('\n')
titles=[]

for table in tables:
    table = ' '.join(table.split())
    titles.append(table.split())


with open('math.csv', 'w') as f:
    for i in range(1,len(links)):
        details=''
        #replace the ',' with '-' in every title
        for j in range(0,len(titles[i])):
            titles[i][j]=titles[i][j].replace(',','-')
            details=details+titles[i][j]

        try:
            f.write(str(i)+' , '+'https://the-eye.eu/public/Books/ManyThings/PDF/'+links[i].get('href')+' , '+'"'+details+'"' +'\n')
        except UnicodeEncodeError:
            print(i)
            pass
    
    
    print('pdfs=====>  : ',i)





    



