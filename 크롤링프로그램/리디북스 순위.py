import os
import datetime
from bs4 import BeautifulSoup
import urllib.request

url = 'https://ridibooks.com/bestsellers/general'
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('a', {'class' : 'title_link'})
    price=soup.find_all('span',{'class':'price'})
    name=soup.find_all('p',{'class':'book_metadata author'})
date= datetime.datetime.today().strftime('%Y%m%d')
desktopPath = os.path.expanduser('~')
filePath = desktopPath +'/Documents/GitHub/Ranking_Archive/data/book/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    for i in range(20) :
        file.write('<div class="rank">'+str(i + 1) + '위</div><div class="title"> ' + items[i+1].get_text(strip = True)+'</div><div class="title">'+name[i+1].get_text(strip = True)+'</div><div class="title">'+price[i+1].get_text(strip = True)+'</div><br>')
