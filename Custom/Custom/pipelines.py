# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import json


import requests,urllib
from Custom.conf.unity import Unity
import codecs

class CustomPipeline(object):

    def process_item(self, item, spider):

        print spider.css['domain_name']
        item['pdf_file'] = self.pdf_files(item['pdf_file'])
        self.save_json(item)

        return item

    def save_json(self,item):

        name = Unity.md5_(item['url'])
        path = '/home/jialele/PycharmProjects/Custom/Custom/files/{0}.json'.format(name)
        with codecs.open(path,'w',encoding='utf-8') as f:
            f.write(json.dumps(dict(item),ensure_ascii=False))


    def pdf_files(self,url):
        req = requests.get(url).content
        return Unity.base64_en(req)

if __name__ == '__main__':
    url = 'beijing.customs.gov.cn/Portals/159/行政处罚/中华人民共和国首都机场海关行政处罚决定书（首关缉违字[2016]446号）.pdf'
    req =requests.get(urllib.quote(url))
    print req.status_code
