import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TaoCrawlPro.items  import TaocrawlproItem
import logging
logger = logging.getLogger(__name__)

class CrawltcSpider(CrawlSpider):
    name = 'crawltc'
    #allowed_domains = ['taoche.com']
    start_urls = ['https://nanjing.taoche.com/bmw/']
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
            item=TaocrawlproItem()
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
            logger.warning(item)
            yield item
