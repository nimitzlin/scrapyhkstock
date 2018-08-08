# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
import pymongo
from scrapy.conf import settings

class StockNamePipeline(object):
	def process_item(self, item, spider):
		if spider.name == "stock":
			line = item["link"] + "\n"
			self.file.write(line)
		return item

	def open_spider(self, spider):
		self.file = open('urls.txt', 'w')

	def close_spider(self, spider):
		self.file.close()


class StockInfoPipeline(object):

        def __init__(self):
            #self.file = open('stock.json', 'wb')
            self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
            self.db = self.client[settings['MONGO_DB']]
            self.coll= self.db[settings['MONGO_COLL']]

	def process_item(self, item, spider):

            d = dict(item)
            if not d.has_key("peratio"):
                raise DropItem("error info in %s" % d)
                
            if "|" in d["peratio"][0]:
                raise DropItem("use less infop in %s" % d)

	    #line = json.dumps(dict(item)) + "\n"
            #self.file.write(line)

            try:
                d["dividend"] = float(d["dividend"][0])
                d["peratio"] = float(d["peratio"][0])
                d["roe"] = float(d["roe"][0][:-1])
            except:
                d["dividend"] = 0
                d["peratio"] = 0
                d["roe"] = 0

            self.coll.insert(d)
            return item

	def close_spider(self, spider):
		#self.file.close()
                pass
