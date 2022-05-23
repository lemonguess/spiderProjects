# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# class ZpproSpiderMiddleware:
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


class ZpproDownloaderMiddleware:
    PROXY_http=[]
    dic = {"ERRORCODE":"0","RESULT":[{"port":"27970","ip":"117.26.42.38"},{"port":"44334","ip":"124.113.216.242"},{"port":"47230","ip":"123.149.39.79"},{"port":"21432","ip":"59.58.224.247"},{"port":"46573","ip":"36.22.79.251"},{"port":"31214","ip":"110.86.136.88"},{"port":"28972","ip":"49.84.120.52"},{"port":"23899","ip":"117.69.24.216"},{"port":"40531","ip":"221.225.53.170"},{"port":"32188","ip":"115.48.87.199"}]}
    for i in range(0,len(dic['RESULT'])):
        ip = f'{dic["RESULT"][i]["ip"]}:{dic["RESULT"][i]["port"]}'
        PROXY_http.append(ip)

    def process_request(self, request, spider):
        print(request.meta)
        ip = self.PROXY_http.pop()
        request.meta['proxy'] = f'https://{ip}'
        print('当前IP为：',f'https://{ip}')
        return None

    # def process_response(self, request, response, spider):
    #     # Called with the response returned from the downloader.
    #
    #     # Must either;
    #     # - return a Response object
    #     # - return a Request object
    #     # - or raise IgnoreRequest
    #     return response

    def process_exception(self, request, exception, spider):
        print('IP连接异常，正在更换IP...')
        request.meta['proxy'] = 'https://' + self.PROXY_http.pop()
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
