import os
import datetime
from bs4 import BeautifulSoup
import urllib.request

url = 'https://music.naver.com/home/index.nhn'
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('span', {'class' : 'm_ell'})
date= datetime.datetime.today().strftime('%Y%m%d')
desktopPath = os.path.expanduser('~')
filePath = desktopPath + '/Documents/GitHub/Ranking_Archive/data/music/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    for i in range(10) :
        file.write('<div class="rank">'+str(i + 1) + '위</div><div class="title">' + items[i*3].get_text(strip = True)+'</div><div class="title">'+ items[i*3+1].get_text(strip = True)+ '</div><br>')
