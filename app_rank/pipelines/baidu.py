# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


MONGODB_SERVER = "127.0.0.1";
MONGODB_PORT = 27017
MONGODB_DB = "app_rank"

import pymongo

from app_rank.items import BaiduappItem

class BaiduappPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            host=MONGODB_SERVER,
            port=MONGODB_PORT,
        )
        self.db = connection[MONGODB_DB]


    def process_item(self, item, spider):
        if isinstance(item, BaiduappItem):
            collection = self.db['baidu']
            collection.update({'url': item.get('url','')}, dict(item), upsert=True)

        return item
