# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

'''
爬虫中间件：暂时不需要，注释掉
'''
#
# class MiddleproSpiderMiddleware:
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
#
import random
# import MyTools.IpPool
from fake_useragent import UserAgent
class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # @classmethod
    # def from_crawler(cls, crawler):
    #     # This method is used by Scrapy to create your spiders.
    #     s = cls()
    #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
    #     return s
    # 封装IP代理池
    PROXY_http=[]

    dic={"ERRORCODE":"0","RESULT":[{"port":"48115","ip":"182.120.246.28"},{"port":"49031","ip":"121.230.252.188"},{"port":"40166","ip":"123.8.254.74"},{"port":"37037","ip":"183.166.125.154"},{"port":"45309","ip":"58.218.116.153"},{"port":"43041","ip":"121.230.88.22"},{"port":"40191","ip":"120.38.126.174"},{"port":"42734","ip":"123.54.233.19"},{"port":"32005","ip":"60.17.249.3"},{"port":"46445","ip":"27.159.164.242"}]}
    for i in range(0,len(dic['RESULT'])):
        ip = f'{dic["RESULT"][i]["ip"]}:{dic["RESULT"][i]["port"]}'
        PROXY_http.append(ip)



    def process_request(self, request, spider):
        '''
        处理请求：拦截请求
        UA伪装
        :param request:
        :param spider:
        :return:
        '''
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        headers = {
            'User-Agent':UserAgent().Chrome
        }
        request.headers['User-Agent'] = headers
        ip=self.PROXY_http.pop()
        # 为了验证代理的操作是否失效：默认是使用本机IP的，这里加一道拦截修改IP,是为了验证def process_exception拦截异常响应函数的修改IP是否成功
        request.meta['proxy'] = f'http://{ip}84512123132'
        print(f'现在使用的IP：http://{ip}')
        return None

    def process_response(self, request, response, spider):
        '''
        拦截响应
        '''
        print(request.headers['User-Agent'])
        # print(request.meta['proxy'])
        return response

    def process_exception(self, request, exception, spider):
        '''
        拦截发生异常的请求对象
        ：当请求发生异常，将会切换ip
        *UA伪装
        代理IP重新设定
        '''
        print('发生异常，重新设定IP')
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_http)
        return request   #将修正之后的请求对象进行重新的请求发送
    #
    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)
