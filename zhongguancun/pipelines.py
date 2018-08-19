# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from scrapy.exceptions import DropItem

# from zhongguancun import settings
import pymongo

class ZhongguancunPipeline(object):

    def __init__(self):
        self.conn = None
        self.db = None


    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.conn.phoneDatabase
        self.coll = self.db.phoneCollection

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
            if valid:
                self.coll.insert(dict(item))
                log.msg("Question Added To MongoDB Successfully!",level=log.DEBUG,spider=spider)
        return item
