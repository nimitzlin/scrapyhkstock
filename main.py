
import scrapy
from twisted.internet import reactor, defer
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from stock.spiders import StockNameSpider, StockInfoSpider 
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':

    configure_logging()
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawlt():
        print "crawl names"
        yield runner.crawl(StockNameSpider.StockNameSpider)
        print "crawl stock info"
        yield runner.crawl(StockInfoSpider.StockInfoSpider)
        reactor.stop()
    crawlt()
    reactor.run() # the script will block here until the last crawl call is finished


