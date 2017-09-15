# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#返回该商品的最大页数
def get_page(name):
    url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'.format(name)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    req = requests.get(url,headers = headers)

    req.encoding = 'utf-8'
    html = BeautifulSoup(req.text,'lxml')
    max_page = html.select('#J_topPage .fp-text i')[0].string
    return int(max_page)*2+1

def Shoop_name(name):
    import MySQLdb
    db = MySQLdb.connect(user='root', password='123456', host='127.0.0.1', db='jd', charset='utf8')
    insert = 'insert into shoop_name(`shoop_name`) values("%s")' % (name)
    cur = db.cursor()
    cur.execute(insert)
    db.commit()
    db.close()


if __name__ == '__main__':
    get_index()