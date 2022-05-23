import scrapy


class GaokaoproSpider(scrapy.Spider):
    name = 'gaokaoPro'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://gkcx.eol.cn/school/search']

    def parse(self, response):
        pass
