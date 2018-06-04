#_*_coding=utf-8_*_
#!/usr/local/python2
### author: Jessie ###
### created on 4th June 2018 ###

import os
import sys
reload(sys)            # python3 doesn't support
sys.setdefaultencoding('utf-8')  # python3 does not support
import requests
import sqlite3
from bs4 import BeautifulSoup

f = open("sina_news.txt", 'a+')
cx = sqlite3.connect('sina_news.db')

cu = cx.cursor()
cu.execute('create table if not exists news (id integer primary key, time, title, href)')

url = "http://news.sina.com.cn/china/"
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

count = 0
for news in soup.select('.news-item'):
    h2 = news.select('h2')
    if len(h2)>0:
        time = news.select('.time')[0].text
        title = h2[0].text
        href = h2[0].select("a")[0]['href']
        f.write(time + '\t' + title + '\t' +href +'\n')
        cu.execute('insert into news values(?,?,?,?)', (count, time, title, href))
        count += 1

f.close()
cu.close()
cx.commit()
cx.close()