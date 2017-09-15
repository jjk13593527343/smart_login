# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import  Request
from scrapy.loader import ItemLoader
from Custom.items import CustomItem,CustomItemLoader


from Custom.conf.BJ_conf import SETTINGS
from Custom.conf.page_get import Urls
from Custom.conf.unity import Unity
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BjcrawlSpider(scrapy.Spider):

    css = SETTINGS['css']
    name = 'bjcrawl'
    page = Urls(SETTINGS).get_page()
    allowed_domains = [SETTINGS['domain_name']]
    start_urls = [SETTINGS['next_page'].format(x) for x in range(page[0],page[1]+1)]




    def parse(self, response):

        urls = ['http://beijing.customs.gov.cn'+x for x in response.css(self.css['index_urls']).extract()]
        for url in urls:
            yield Request(url,callback=self.parse_info)

    def parse_info(self,response):
        pdf_file = self.css['domain_name']+response.css(self.css['pdf_file']).extract_first()
        item = CustomItemLoader(item = CustomItem(),response=response)
        item.add_css('title',self.css['title'])
        item.add_css('date',self.css['date'])
        item.add_value('pdf_file',pdf_file)
        item.add_css('Punishment_doc',self.css['Punishment_doc'])
        item.add_value('party',self.css['party'])
        item.add_value('content_type',self.css['content_type'])
        item.add_value('base64_type', self.css['base64_type'])
        item.add_value('url', response.url)
        item.add_value('domain_name',self.allowed_domains[0])


        yield item.load_item()
