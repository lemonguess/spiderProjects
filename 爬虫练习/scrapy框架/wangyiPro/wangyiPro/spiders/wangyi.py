import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
import logging
logger = logging.getLogger(__name__)
import re
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    modle_urls = []#存储五个板块对应的详情页url
    #解析五大板块对应的详情页URL


    #实例化一个浏览器对象
    def __init__(self):

        # 防止打印一些无用的日志
        from selenium.webdriver.chrome.options import Options
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                                    chrome_options=self.chrome_options)
    def parse(self, response):
        li_list = response.xpath('//*[@id="js_festival_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [2,3]
        for index in alist:
            modle_url = li_list[index].xpath('./a/@href').extract_first()
            self.modle_urls.append(modle_url)
        # 依次对每一个板块对应的页面进行请求
        for url in self.modle_urls:#对每一个板块的url进行请求发送
            #这里请求发送的是request对象，封装了一个request对象给引擎
            yield scrapy.Request(url=url,callback=self.parse_modle)

    #每一个板块对应的新闻标题相关的内容都是动态加载出来的
    def parse_modle(self,response):#解析每一个板块页面中对应新闻的标题和新闻详情页的url
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_details_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyiproItem()
            item['title'] = title
            #对新闻详情页的url发起请求
            #logger.warning(f'标题：{title}：{new_details_url}')
            yield scrapy.Request(url=new_details_url,callback=self.parse_detail,meta={'item':item})
            '''
            url:请求地址
            callback:请求响应数据的处理函数
            meta:传递数据
                 每次请求都会携带meta参数{'item':item}，
                 传递给响应，response响应对象就会具有
                 response.meta=meta
                 获取：response.meta['item']
           '''
    def parse_detail(self,response):
        '''
        对新闻详情页内容进行解析
        '''
        content = response.xpath('/html/body/div[2]/div[1]/div[3]/div[2]//text()').extract()
        content = ''.join(content)
        content = re.sub('\n','',content)

        item = response.meta['item']
        item['content'] = content
        logger.warning(item)
        yield item

    def closed(self,spider):
        self.bro.quit()
