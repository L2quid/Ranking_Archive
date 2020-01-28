import os
import datetime
from bs4 import BeautifulSoup
import urllib.request
date= datetime.datetime.today().strftime('%Y%m%d')
url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date='+date
with urllib.request.urlopen(url) as fs :
    soup = BeautifulSoup(fs.read().decode(fs.headers.get_content_charset()), 'html.parser')
    items = soup.find_all('div', {'class' : 'ranking_headline'})
    links=soup.find_all('a',{'class':'nclicks(rnk.sci)'})
   
desktopPath = os.path.expanduser('~')
filePath = desktopPath + '/Documents/GitHub/Ranking_Archive/data/ITnews/'+str(date)+'.txt'
with open( filePath, 'w+',encoding='utf-8') as file:
    file.write('<h3>'+date+'의 뉴스입니다.</h3>')
    for i in range(20) :
        file.write('<div class="wrap"><div class="rank">'+str(i + 1) + '위</div> <div class="title">' + items[i].get_text(strip = True)+'</div><a class="link" href="'+str('https://news.naver.com')+links[2*i].attrs['href']+'"> 이동</a>'+'</div>')
        
