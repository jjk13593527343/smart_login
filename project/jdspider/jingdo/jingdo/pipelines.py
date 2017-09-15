# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class JingdoPipeline(object):

    def __init__(self,crawler):
        self.db = MySQLdb.Connect(
            user = crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DB'),
            charset='utf8'
        )
        self.cur = self.db.cursor()

    @classmethod
    def from_crawler(cls, crawler):

        return cls(crawler)

    def process_item(self, item, spider):
        insert,data = item.insert()
        self.cur.execute(insert,data)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
