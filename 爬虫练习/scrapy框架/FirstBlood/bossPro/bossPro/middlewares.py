# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


import random
from scrapy.http import HtmlResponse
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
class BossproDownloaderMiddleware:




    def process_request(self, request, spider):

        #print(request.meta['proxy'])

        return None

    def process_response(self, request, response, spider):
        '''
        拦截五大板块的对应的响应对象进行篡改
        挑选出指定的响应对象进行篡改（后五个请求）
        通过指定request  :  request.url
        通过request指定response  :spider.modle_urls
        self.spider：爬虫对象
        '''
        # bro = spider.bro  # 获取了在爬虫类中定义的浏览器对象
        #
        # print("正在打开网页... ...")
        # sleep(3)
        # if request.url in spider.start_urls:
        #     bro.get(request.url)
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        # else:
        #     return response
        spider.bro.get(request.url)
        page_text = spider.bro.page_source
        new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        return new_response

        # if request.url in spider.start_urls :
        #     '''
        #     #response——五大板块对应的响应对象
        #     #针对定位到的这些response进行篡改
        #     #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代旧的，原来不满足需求的response
        #     #如何获取动态加载出的新闻数据？
        #         1.基于selenium便捷的获取动态加载数据
        #
        #     '''
        #     bro.get('https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&city=100010000&industry=&position=')
        #     #bro.get(request.url)
        #     print("正在打开首页... ...")
        #     sleep(2)
        #     page_text = bro.page_source  # 包含了动态加载的新闻数据
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response
        #     print('已获得首页动态response')
        # else:
        #     bro.get('https://blog.csdn.net/weixin_30496431/article/details/94857575')
        #     #bro.get(request.url)
        #     sleep(2)
        #     page_text = bro.page_source  # 包含了动态加载的新闻数据
        #     new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        #     return new_response


    def process_exception(self, request, exception, spider):
        # IP = random.choice(self.PROXY_http)
        # proxy='http://' +IP
        # chrome_options = Options()
        # chrome_options.add_argument(f'--proxy-server={proxy}')
        # chrome_options.add_argument(
        #     f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36')
        # bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
        #                       chrome_options=chrome_options)
        # bro.get(request.url)
        # #request.meta['proxy'] = 'http://' +IP
        # print('出现连接错误，正在切换IP:',IP)
        #
        # print("正在打开网页... ...")
        # sleep(3)
        # page_text = bro.page_source
        # new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
        return None

