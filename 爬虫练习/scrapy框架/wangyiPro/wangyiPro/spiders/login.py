import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
