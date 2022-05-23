import scrapy


class ModenskySpider(scrapy.Spider):
    name = 'modensky'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.modernsky.com/home/artists']

    def parse(self, response):
        pass
