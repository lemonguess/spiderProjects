# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# class JobsproSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


from JobsPro.spiders.jobs import JobsSpider
from scrapy.http import HtmlResponse
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import random

class JobsproDownloaderMiddleware:


    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):
        bro = spider.bro
        bro.get(request.url)
        sleep(2)
        page_text = bro.page_source  # 包含了动态加载的新闻数据
        response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        return response

    def process_exception(self, request, exception, spider):
        PROXY_http = []
        dic = {"ERRORCODE":"0","RESULT":[{"port":"31798","ip":"123.55.4.219"},{"port":"36918","ip":"117.95.198.117"},{"port":"26767","ip":"123.162.4.189"},{"port":"32029","ip":"114.239.123.104"},{"port":"25099","ip":"180.104.55.199"},{"port":"35406","ip":"49.68.102.30"},{"port":"48565","ip":"222.88.122.109"},{"port":"22466","ip":"60.182.33.205"},{"port":"25992","ip":"117.31.45.58"},{"port":"38066","ip":"123.162.3.241"}]}
        for i in range(0, len(dic['RESULT'])):
            ip = f'{dic["RESULT"][i]["ip"]}:{dic["RESULT"][i]["port"]}'
            PROXY_http.append(ip)
        IP = random.choice(PROXY_http)
        proxy='http://' +IP

        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument(
            f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36')
        print('错误，更换IP：',IP)
        self.bro=webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                              chrome_options=chrome_options)
        self.bro.get(request.url)
        sleep(2)
        page_text = self.bro.page_source  # 包含了动态加载的新闻数据
        response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        return response

