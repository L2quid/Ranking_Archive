import os
desktopPath = os.path.expanduser('~/Documents/GitHub/Ranking_Archive/크롤링프로그램/')
files=['IT뉴스TOP30','네이버영화순위','리디북스순위','벅스음악순위']
for file in files:
    os.startfile(desktopPath +file+'.py')

