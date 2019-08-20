import os
import datetime
from bs4 import BeautifulSoup
import urllib.request

url = 'https://movie.naver.com/movie/running/current.nhn'
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('dt', {'class' : 'tit'})
    images=[]
    for img in soup.findAll('img'):
        images.append(img.get('src'))
date= datetime.datetime.today().strftime('%Y%m%d')
desktopPath = os.path.expanduser('~')
filePath = desktopPath + '/Documents/GitHub/Ranking_Archive/data/movie/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    file.write('<h3>'+date+'의 영화 순위입니다.</h3>')
    for i in range(20) :
        file.write('<div class="wrap"><div class="rank">'+str(i + 1) + '위</div><img src="'+images[i+74]+'"><div class="title"> ' +items[i].contents[3].get_text(strip = True)+'</div></div><br>')
