import os
import datetime
from bs4 import BeautifulSoup
import urllib.request
date= datetime.datetime.today().strftime('%Y%m%d')
url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate='+date
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('p', {'class' : 'title'})
    names=soup.find_all('p', {'class' : 'artist'})
    images=[]
    for img in soup.findAll('img',src=True):
        images.append(img.get('src'))
desktopPath = os.path.expanduser('~')
filePath = desktopPath + '/Documents/GitHub/Ranking_Archive/data/music/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    file.write('<h3>'+date+'의 음악 순위입니다.</h3>')
    for i in range(20) :
        file.write('<div class="wrap"><div class="rank">'+str(i + 1) + '위</div><img src="'+str(images[i+17])+'"><div class="title">' + items[i].get_text(strip = True)+'</div><div class="title">'+ names[i].get_text(strip = True)+ '</div></div>')
