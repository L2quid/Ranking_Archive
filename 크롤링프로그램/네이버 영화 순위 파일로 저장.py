import os
import datetime
from bs4 import BeautifulSoup
import urllib.request

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('div', {'class' : 'tit3'})
    date= datetime.datetime.today().strftime('%Y%m%d')
desktopPath = os.path.expanduser('~')
filePath = desktopPath + '/Documents/GitHub/Ranking_Archive/data/movie/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    for i in range(20) :
        file.write('<div class="rank">'+str(i + 1) + '위</div><div class="title"> ' + items[i].get_text(strip = True)+'</div><br>')
