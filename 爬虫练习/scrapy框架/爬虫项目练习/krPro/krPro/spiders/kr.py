import scrapy
import json
from ..items import KrproItem
#from krPro.items import DetailItem
from lxml import etree
import logging
logger = logging.getLogger(__name__)
import copy

class KrSpider(scrapy.Spider):


    name = 'kr'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://gateway.36kr.com/api/mis/nav/search/resultbytype']

    def __init__(self):
        self.pageEvent = 1
        self.searchWord = input("=>>打算查什么内容哇？")


        self.pageSize = int(input("=>>行，要多少篇？"))
        # print(type(self.searchWord))
        # print(type(self.pageSize))
        # self.searchWord = "奥运会"
        #
        # self.pageSize = 2
        # print(type(self.summm))
        #
        # while True:
        #
        #     if isinstance(self.summm,int(self.summm)):
        #         self.pageSize=self.summm
        #
        #
        #     else:
        #         self.summm = input("=>>你会不会打字？")

        self.platformId = 2
        self.searchType = "article"

        self.siteId = 1
        self.Request_Payload = {
            "param": {
                "pageCallback": "eyJmaXJzdElkIjoxMzI4ODQ1Nzg2ODQxNzM2LCJsYXN0SWQiOjEzMjc0NTM1NTM5MjQwOTcsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzM4NjYxMjAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcyOTc1MTUwMDB9",
                "pageEvent": self.pageEvent,
                "pageSize": self.pageSize,
                "platformId": self.platformId,
                "searchType": self.searchType,
                "searchWord": self.searchWord,
                "siteId": self.siteId,
                "sort": "date"},
            "partner_id": "web",
            "timestamp": "1627469455770"
        }
    def start_requests(self):
        url = self.start_urls[0]

        headers = {
            'authority': 'gateway.36kr.com',
            'method': 'POST',
            'path': '/api/mis/nav/search/resultbytype',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            #'content-length': '346',
            # 'cookie': 'Hm_lvt_1684191ccae0314c6254306a8333d090=1627469447; Hm_lpvt_1684191ccae0314c6254306a8333d090=1627469447; Hm_lvt_713123c60a0e86982326bae1a51083e1=1627469447; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1627469447; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217aecbcffa51fe-0d9880bc07d69d-4373266-1327104-17aecbcffa6186%22%2C%22%24device_id%22%3A%2217aecbcffa51fe-0d9880bc07d69d-4373266-1327104-17aecbcffa6186%22%2C%22props%22%3A%7B%7D%7D',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
            'origin': 'https://36kr.com',
            'pragma': 'no-cache',
            'referer': 'https://36kr.com/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site'

        }
        yield scrapy.http.Request(url=url,body=json.dumps(self.Request_Payload),callback=self.parse,method='POST',
                             dont_filter=True,
                             headers=headers,
                             errback=self.errback)

    def errback(self, response):
            print(response)
            print('哦豁，啥几把也没有')

    def parse(self, response):
        item_list = json.loads(response.text)["data"]["itemList"]
        '''
         {
        "itemId": 1329091545520390,
        "widgetTitle": "韩束、鸿星尔克野性消费启示录",
        "widgetImage": "https://img.36krcdn.com/20210728/v2_cd4752c703994c8bb95bfacddb7b523c_img_png",
        "publishTime": 1627480831000,
        "route": "detail_article?itemId=1329091545520390",
        "content": "而这一次临近<em>奥</em><em>运</em><em>会</em>，他的团队在快手借势推出辛选奥运好物直播季。 水能载舟，亦能覆舟。 虽然说这些热点，可以为电商直播引流，将舆论场转变为大卖场，但是同样也会将带货主播推向风口浪尖。"
      },'''
        item = KrproItem()
        for items in item_list:
            detail_url = f'https://36kr.com/p/{items["itemId"]}'
            Title = items["widgetTitle"]
            img_url = items["widgetImage"]
            item['detail_url'] = detail_url
            item['Title'] = Title
            item['img_url'] = img_url

            yield item

            yield scrapy.Request(url=detail_url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'},
                                 dont_filter=True,callback=self.parse_detail,meta={'item':copy.deepcopy(item)})
    def parse_detail(self,response):

        item=response.meta['item']

        Title =item['Title']
        tree = etree.HTML(response.text)
        content = f'【标题：{Title}】\n\n'+''.join(tree.xpath('//div[@class="common-width content articleDetailContent kr-rich-text-wrapper"]//text()'))
        #logger.warning('正在线上读取文章... ...')

        item['content'] = content
        logger.warning(content)
        yield item


        #print(content)


