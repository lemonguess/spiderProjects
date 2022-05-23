import scrapy
from selenium import webdriver
from bossPro.items import BossproItem
from selenium.webdriver.chrome.options import Options
from time import sleep

class BossproSpider(scrapy.Spider):
    name = 'bossPRo'
    start_urls =['https://www.zhipin.com/c101190100/?query=%E7%88%AC%E8%99%AB&page=1&ka=page-1']

    #allowed_domains = ['www.xxx.com']
    # for page in range(1,6):
    #     boss_url = f'https://www.zhipin.com/c101190100/?query=%E7%88%AC%E8%99%AB&page={page}&ka=page-{page}'
    #     start_urls.append(boss_url)
    # print(start_urls)
    #实例化一个浏览器对象
    def __init__(self):

        # 防止打印一些无用的日志
        print('开始实例化浏览器... ...')
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                                    chrome_options=self.chrome_options)
        sleep(10)
        print('浏览器实例化完成.')
        sleep(2)
    def parse(self, response):
        '''
        初始化Item:Boss
        :param response:
        :return:
        '''
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')

        # print(response.page_source)
        for li in li_list:
            item = BossproItem()
            item['job'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a/test()').extract_first()
            item['place'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/span/test()').extract_first()
            item['salary'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[2]/span/test()').extract_first()
            item['year'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[2]/p//test()').extract_first()
            item['c_name'] = li.xpath('./div[1]/div[1]/div[2]/div[1]/h3/a/test()').extract_first()
            item['fuli'] = li.xpath('./div[1]/div[2]/div[2]/test()').extract_first()

            detail_url ='https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href').extract_first()

            # self.detail_urls.append(detail_url)
            print (item)
            yield item
            #yield  scrapy.Request(url=detail_url,callback=self.parse_modle,meta={'item':item})
    #     # 依次对每一个板块对应的页面进行请求
    #     for url in self.detail_urls:#对每一个板块的url进行请求发送
    #         #yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item})
    #         yield scrapy.Request(url=url, callback=self.parse_detail)
    #     print(self.detail_urls)
    #
    # def parse_detail(self,response):
    #     item_detail = BossproItem2()
    #     item_detail['zhiweimiaoshu'] = zhiweimiaoshu
    #     item_detail['zhiweimiaoshu'] = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//test()').extract()
    #     item = response.meta['item']
    #     item['zhiweimiaoshu'] =  item_detail
    #     #print(item_detail['zhiweimiaoshu'])
    #     print(item)
    #     yield item

    # def closed(self,spider):
    #     self.bro.quit()