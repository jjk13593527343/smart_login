# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


from Custom.conf.unity import Unity

class CustomItemLoader(ItemLoader):

    default_output_processor = TakeFirst()



class CustomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(remove_tags)
    )
    date = scrapy.Field(
        input_processor = MapCompose(Unity.date_edit)
    )
    pdf_file = scrapy.Field()
    Punishment_doc = scrapy.Field(
        input_processor=MapCompose(Unity.Punishment_doc)
    )
    Punishment_com =scrapy.Field()
    party = scrapy.Field()
    content_type = scrapy.Field()
    base64_type = scrapy.Field()
    url = scrapy.Field()
    domain_name = scrapy.Field()