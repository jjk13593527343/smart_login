#-*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from Custom.conf.unity import Unity
from Custom.conf.BJ_conf import SETTINGS


class Urls(object):
    def __init__(self,settings):

        self.afg = settings


    def get_page(self):

        req = requests.get(self.afg['url'])

        return self.parse_info(req.text)

    def parse_info(self,text):

        html = BeautifulSoup(text,'lxml')
        html = BeautifulSoup(text, 'lxml')
        next_page = [x.get_text() for x in html.select(self.afg['css']['next_page'])][0]
        return [int(x) for x in Unity.max_page(next_page)]



if __name__ == '__main__':
    print Urls(SETTINGS).get_page()