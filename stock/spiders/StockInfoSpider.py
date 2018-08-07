import scrapy

from stock.items import StockItem
from scrapy.http import Request

from scrapy_splash import SplashRequest

class StockInfoSpider(scrapy.Spider):
	name = "stockinfo"

        def __init__(self):
            self.start_urls = ""
            self.urls = []
            super(StockInfoSpider, self).__init__()
            with open("urls.txt") as urls:
                for url in urls:
                    url = url.strip('\n')
                    self.urls.append(url) 

        def start_requests(self):
            splash_args = {
                                'wait': 0.5,
            }
            for start_url in self.urls:
                request = SplashRequest(start_url, self.parse, endpoint='render.html', args=splash_args)
                yield request

	def parse(self, response):

            for sel in response.xpath('//div[@id="base_info"]//ul//li'):
                    print sel.extract()
                    item = StockItem()
                    yield item
