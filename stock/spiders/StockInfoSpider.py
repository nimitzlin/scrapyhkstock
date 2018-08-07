# -*- coding: utf-8 -*-
import scrapy

from stock.items import StockItem
from scrapy.http import Request

from scrapy_splash import SplashRequest
import re

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
            # use splash to render js
            splash_args = {
                                'wait': 0.5,
            }
            for start_url in self.urls:
                request = SplashRequest(start_url, self.parse, endpoint='render.html', args=splash_args)
                yield request

	def parse(self, response):
        
            #for sel in response.xpath('//div[@id="base_info"]//ul//li'):
            #        print sel.extract()
            #       #例如获取股息率 市盈率  
            #        item = StockItem()
            #        yield item
            res_td = r'<td>(.*?)</td>'
            for sel in response.xpath('//table[@id="financial_analysis"]//tr'):
                    self.index = 0
                    item = StockItem()
                    link = response.url
                    item["link"] = link
                    item["num"] = link.split("/")[-1][:-5]
                    for trinfo in sel.xpath('td[not(contains(@class, "showRedTips"))]'):
                        self.index += 1
                        if self.index == 6:
                            line = trinfo.extract()
                            m_td = re.findall(res_td, line, re.S|re.M)
                            item["peratio"] = m_td
                        elif self.index == 10:
                            line = trinfo.extract()
                            m_td = re.findall(res_td, line, re.S|re.M)
                            item["roe"] = m_td
                        elif self.index == 11:
                            line = trinfo.extract()
                            m_td = re.findall(res_td, line, re.S|re.M)
                            item["dividend"] = m_td
                    if self.index == 11:
                        yield item
                    else:
                        continue

