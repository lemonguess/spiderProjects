import scrapy
from selenium import webdriver
from JobsPro.items import JobsproItem
from selenium.webdriver.chrome.options import Options
import random

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls =[]
    detail_urls=[]

    #allowed_domains = ['www.xxx.com']
    for page in range(1,2):
        boss_url = f'https://www.zhipin.com/c101190100/?query=%E7%88%AC%E8%99%AB&page={page}&ka=page-{page}'
        start_urls.append(boss_url)
    def __init__(self):
        PROXY_http = []
        dic = {"ERRORCODE":"0","RESULT":[{"port":"27001","ip":"183.155.118.116"},{"port":"30585","ip":"123.10.64.136"},{"port":"23544","ip":"27.158.47.114"},{"port":"37146","ip":"1.194.32.249"},{"port":"40072","ip":"49.70.17.147"},{"port":"43939","ip":"60.166.75.203"},{"port":"31453","ip":"123.54.22.36"},{"port":"32579","ip":"59.47.230.154"},{"port":"46409","ip":"36.27.142.176"},{"port":"40444","ip":"27.152.193.170"}]}
        for i in range(0, len(dic['RESULT'])):
            ip = f'{dic["RESULT"][i]["ip"]}:{dic["RESULT"][i]["port"]}'
            PROXY_http.append(ip)
        IP = random.choice(PROXY_http)
        proxy='http://' +IP

        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument(
            f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36')
        print('当前的IP是：',IP)
        self.bro=webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                              chrome_options=chrome_options)
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = JobsproItem()
            item['job'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a/test()').extract_first()
            item['place'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/span/test()').extract_first()
            item['salary'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[2]/span/test()').extract_first()
            item['year'] = li.xpath('./div[1]/div[1]/div[1]/div[1]/div[2]/p//test()').extract_first()
            item['c_name'] = li.xpath('./div[1]/div[1]/div[2]/div[1]/h3/a/test()').extract_first()
            item['fuli'] = li.xpath('./div[1]/div[2]/div[2]/test()').extract_first()

            detail_url ='https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href').extract_first()

            self.detail_urls.append(detail_url)
            yield item
