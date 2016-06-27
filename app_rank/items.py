# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduappItem(scrapy.Item):
    # define the fields for your item here like:
    data_source = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    download_num = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()


class AppleAppItem(scrapy.Item):
    data_source = scrapy.Field()
    order = scrapy.Field()
    image_url = scrapy.Field()
    download_url = scrapy.Field()
    name = scrapy.Field()
    app_type = scrapy.Field()
