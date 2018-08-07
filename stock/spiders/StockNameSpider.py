import scrapy

from stock.items import StockItem

class StockNameSpider(scrapy.Spider):
	name = "stock"
	start_urls = [
			"http://quote.eastmoney.com/hk/HStock_list.html",
	]


	def parse(self, response):
                self.count = 0
		
		for sel in response.xpath('//li//a[contains(@href, "http://quote.eastmoney.com/hk")]/@href'):
                        #debug
                        if self.count >= 3:
                            continue
                        #debug
			link = sel.extract()
			num = link.split("/")[-1].split(".")[0]
			if num.isdigit():
				num = int(num)
			else:
				continue
			item = StockItem()
			item['num'] = num
			item['link'] = link
                        self.count += 1
			yield item
