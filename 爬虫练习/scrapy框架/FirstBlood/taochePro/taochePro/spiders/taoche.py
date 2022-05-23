import scrapy
from taochePro.items import TaocheproItem
from taochePro.items import TaocheParamenterConfig
import logging
logger = logging.getLogger(__name__)
import re
class TaocheSpider(scrapy.Spider):
    name = 'taoche'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://nanjing.taoche.com/audi/?page=1&#pagetag']
    #url模板
    url = 'https://nanjing.taoche.com/audi/?page=%d'

    def parse(self, response):
        #最大页数
        max_page = response.xpath('//*[@id="containerId"]/div[1]/div[7]/div/div/a[last()-1]/text()').extract_first()
        # logger.warning(max_page)
        #for page in range(1, 2):
        for page in range(1,int(max_page)+1):
            '''
                手动请求每一页，将url地址传递给调度器
                url：请求地址
                callback：请求后的数据响应的处理函数
                meta:传递数据
                    每次请求组都会携带meta参数{'page':page}
                    response.meta = meta
                    response.meta['page']
            '''
            new_url = self.url % page
            yield scrapy.Request(url=new_url,callback=self.parse_taoche,meta={'page':page})



    def parse_taoche(self, response):
        #logger.warning(f'{response.meta["page"]}')
        #依次得到了每一页的汽车列表
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
            yield item
            # logger.warning(item)

            #获取每一辆车的详情页URl
            detail_url = car.xpath('./div[1]/div/a/@href').extract_first()
            # logger.warning(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        attrs = response.xpath('/html/body/div[9]/div[1]/div[2]/div[4]/div/dl[3]/dd/text()').extract_first()
        display,transmission=tuple(attrs.split('/'))

        item_detail = TaocheParamenterConfig()
        item_detail['display']=display
        item_detail['transmission'] = transmission
        item = response.meta['item']
        item['detail'] = item_detail
        logger.warning(item)
        yield item




