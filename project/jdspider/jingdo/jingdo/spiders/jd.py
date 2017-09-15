# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from jingdo.unity.page_cralw import get_page,Shoop_name
from scrapy_redis.spiders import RedisSpider
import re
from urllib.parse import urljoin
import json,time
from ..items import Shoop_Info,Shoop_Comment
from jingdo.settings import SHOOP_NAME


class JdSpider(RedisSpider):
    name = 'jd'
    allowed_domains = ['search.jd.com','item.jd.com','p.3.cn','club.jd.com']
    shoop = SHOOP_NAME

    #获取最大列表页
    max_page = get_page(shoop)

    #列表url
    urls = 'https://search.jd.com/Search?keyword={shoop}&enc=utf-8&page={page}&s=54&scrolling=y'

    #价格接口
    price_url = 'https://p.3.cn/prices/mgets?skuIds=J_{id}'

    #评论接口
    conment_url = 'https://club.jd.com/comment/productPageComments.action?productId={id}&score=0&sortType=5&page={page}&pageSize=10'

    #请求列表页
    def start_requests(self):
        Shoop_name(self.shoop)
        for page in range(1,self.max_page):
            yield Request(url=self.urls.format(shoop=self.shoop,page=page))


    #解析每页的
    def parse(self, response):
        data = response.css('#J_goodsList .gl-warp.clearfix .gl-item')
        r = '//item.jd.com/(.*?).html'
        for info in data:
            url = info.css('.gl-i-wrap .p-name.p-name-type-2 a::attr(href)').extract_first()
            title = info.css('.gl-i-wrap .p-name.p-name-type-2 a em::text').extract_first()
            shoop_id = re.match(r,url).group(1)
            print(shoop_id)
            if title:
                yield Request(url=self.price_url.format(id=shoop_id),meta={'url':url,'title_name':title,'shoop_id':shoop_id},callback = self.parseSshoopInfo)


    #解析评论信息
    def parseConment(self,respomse):
        item = Shoop_Comment()
        page = respomse.meta.get('page')
        shoop_id = respomse.meta.get('id')
        comment = json.loads(respomse.text)
        max_page = comment['maxPage']
        comment_data = comment['comments']

        for comment_info in comment_data:
            nickname = comment_info['nickname']
            content = comment_info['content']
            creationTime = comment_info['creationTime']
            item['shoop_id'] = shoop_id
            item['nickname'] = nickname
            item['content'] = content
            item['creationTime'] = creationTime
            print(nickname,shoop_id)
            yield item
        if page != max_page:
            yield Request(url=self.conment_url.format(id=shoop_id,page=page+1),meta={'page':page+1,'id':shoop_id},callback=self.parseConment)

    #解析商品信息
    def parseSshoopInfo(self,response):
        item = Shoop_Info()
        shoop_title = response.meta.get('title_name')
        shoop_id = response.meta.get('shoop_id')
        print(shoop_id)
        shoop_url = response.meta.get('url')
        shoop_price = json.loads(response.text[1:-2])['op']
        item['shoop_title'] =shoop_title
        item['shoop_url'] = shoop_url
        item['shoop_price'] = shoop_price
        item['shoop_id'] = shoop_id
        item['shoop_name'] = self.shoop
        yield item
        yield Request(url=self.conment_url.format(id=shoop_id, page=0), meta={'page': 0, 'id': shoop_id},
                      callback=self.parseConment)
