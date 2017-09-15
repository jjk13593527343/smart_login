# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Shoop_Name(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shoop_name = scrapy.Field()
    def inser(self):
        insert = 'insert into shoop_name(shoop_name) values(%s)'
        data = (self['shoop_name'])
        return insert,data

class Shoop_Info(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shoop_title = scrapy.Field()
    shoop_url = scrapy.Field()
    shoop_price = scrapy.Field()
    shoop_id = scrapy.Field()
    shoop_name = scrapy.Field()
    def insert(self):
        insert = 'insert into shoop_info(`shoop_title`,`shoop_url`,`shoop_price`,`shoop_id`,`shoop_name`) values(%s,%s,%s,%s,%s)'
        data = (self['shoop_title'],self['shoop_url'],self['shoop_price'],self['shoop_id'],self['shoop_name'])
        return (insert,data)
class Shoop_Comment(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shoop_id = scrapy.Field()
    nickname  = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    def insert(self):
        insert = 'insert into shoop_comment(`shoop_id`,`nike_name`,`content`,`createDate`) values(%s,%s,%s,%s)'
        data = (self['shoop_id'], self['nickname'], self['content'], self['creationTime'])
        return (insert, data)