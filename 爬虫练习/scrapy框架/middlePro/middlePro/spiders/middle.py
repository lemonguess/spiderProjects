import scrapy


class MiddleSpider(scrapy.Spider):
    '''
    需求：请求拦截，设定user_agent，代理ip的更改
         爬取百度
    '''
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6']

    def parse(self, response):
        print(response)
        # page_text = response.test
        #
        # with open('ip.html','w',encoding='utf-8') as fp:
        #     fp.write(page_text)
