# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

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
	def process_item(self, item, spider):
		return item
