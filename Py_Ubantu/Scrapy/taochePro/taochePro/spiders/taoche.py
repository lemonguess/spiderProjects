import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import TaocheproItem

class TaocheSpider(RedisCrawlSpider):
    name = 'taoche'
    #allowed_domains = ['taoche.com']#注释起来，不做域名限制
    #start_urls = ['http://taoche.com/']#起始的urls应该从公共调度器取用（Redis）
    redis_key = 'taoche' #会去redis（公共调度器里面获取key为taoche的数据 taoche:[]），相当于strat_urls列表
    '''
    对公用调度器的要求：1.每台机器都可以进行连接：需要是一个网络服务
                    2.能够进行存储，要爬取url:数据库
                    3.队列模型{    mysql:二维表
                                 redis:文档接口{
                                            字符串
                                            列表{LPUSH:栈
                                                RPUSH:√队列，先进先出}
                                            哈希
                                            集合：唯一，可实现去重
                                            有序集合
                                            }
                                 mongoDB:json文档
                    4.去重        }
    redis还可以存储item
    '''
    link='/\?page=\d+?#pagetag'
    #定义路由规则
        #LinkExtractor链接提取器，根据正则规则提取url地址 stat_urls
        #callback 提取出来的url地址发送请求，获取响应，会把响应对象给callback指定的函数进行处理
        #follow 获取的响应页面是否再次经过rules来进行提取urls
    rules = (
        Rule(LinkExtractor(allow=link), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        car_list = response.xpath('//*[@id="container_base"]/ul/li')
        for car in car_list:
            item=TaocheproItem()
            lazyimg = car.xpath('./div[1]/div/a/img/@src').extract_first()
            title = car.xpath('./div[1]/div[1]/a/@title').extract_first()
            resisted_data = car.xpath('./div[2]/p/i[1]/text()').extract_first()
            mileage = car.xpath('./div[2]/p/i[2]/text()').extract_first()
            city = car.xpath('./div[2]/p/i[3]/text()').extract_first()
            city = re.sub('\s+', '', city).strip()
            price = car.xpath('./div[2]/div[1]/i//text()').extract_first()
            item['lazyimg']=lazyimg
            item['title']=title
            item['resisted_data']=resisted_data
            item['mileage']=mileage
            item['city']=city
            item['price']=price
            print(item)
            yield item
