import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://dk.sun0769.com/mail/?ac=list&tid=1']

    #链接提取器：根据指定规则(allow="正则")，进行指定链接的提取
    link = 'http://dk.sun0769.com/mail/'+LinkExtractor(allow=r'?ac=list&tid=1&order=1&page=\d+')

    rules = (
        #规则解析器——实例化了规则解析器的对象（LinkExtractor：链接提取器）
                #作用:将链接提取器提取到的链接，进行指定规则的解析操作(每调用一次，就会对某一个链接进行解析)
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
