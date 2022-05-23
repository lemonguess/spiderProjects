import scrapy
import re


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://nanjing.anjuke.com/']

    def parse(self, response):
        page_text = response.text
        with open('HomePage.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        print(page_text)
