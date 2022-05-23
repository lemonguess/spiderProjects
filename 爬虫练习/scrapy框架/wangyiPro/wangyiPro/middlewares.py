# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep

class WangyiproDownloaderMiddleware:


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        '''
        拦截五大板块的对应的响应对象进行篡改
        挑选出指定的响应对象进行篡改（后五个请求）
        通过指定request  :  request.url
        通过request指定response  :spider.modle_urls
        self.spider：爬虫对象
        '''
        bro = spider.bro  # 获取了在爬虫类中定义的浏览器对象
        if request.url in spider.modle_urls:
            '''
            #response——五大板块对应的响应对象
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代旧的，原来不满足需求的response
            #如何获取动态加载出的新闻数据？
                1.基于selenium便捷的获取动态加载数据
                
            '''
            bro.get(request.url)
            sleep(2)
            page_text = bro.page_source  #包含了动态加载的新闻数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            response #其他请求对应的url


        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass


