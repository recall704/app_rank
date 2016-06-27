# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


MONGODB_SERVER = "127.0.0.1";
MONGODB_PORT = 27017
MONGODB_DB = "app_rank"

import pymongo

from app_rank.items import AppleAppItem

class AppleappPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            host=MONGODB_SERVER,
            port=MONGODB_PORT,
        )
        self.db = connection[MONGODB_DB]


    def process_item(self, item, spider):
        if isinstance(item, AppleAppItem):
            collection = self.db['apple']
            collection.update({'download_url': item.get('download_url','')}, dict(item), upsert=True)

        return item