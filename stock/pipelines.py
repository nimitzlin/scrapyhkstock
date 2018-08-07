# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem

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
            self.file = open('stock.json', 'wb')

	def process_item(self, item, spider):

            d = dict(item)
            if "|" in d["peratio"][0]:
                raise DropItem("use less infop in %s" % d)

	    line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item

	def close_spider(self, spider):
		self.file.close()
