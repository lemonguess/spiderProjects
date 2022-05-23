import scrapy
from imagePro.items import ImageproItem
import logging
logger = logging.getLogger(__name__)

class ImgproSpider(scrapy.Spider):

    name = 'imgPro'
    #allowed_domains = ['www.xxx.com']
    # start_urls = ['https://pic.netbian.com/4kdongman/']
    start_urls  = ['https://pic.netbian.com/4kdongman/']
    for i in range(2,4):
        url = f'https://pic.netbian.com/4kdongman/index_{i}.html'
        start_urls.append(url)
    # print(start_urls)
    # global src_list
    # src_list = []



    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div/div[3]/ul/li')

        # global src_list
        # global src
        # global img_name

        for li in li_list:

            # if li.xpath('./a/img/@src').extract_first() and li.xpath('./a/b/test()').extract_first() is not None:
            src ='https://pic.netbian.com' + li.xpath('./a/img/@src').extract_first()

            img_name = li.xpath('./a/b/text()').extract_first()
            print(src)
            logger.warning(src)
            dic = {'img_name':img_name+'.png','src':src}
            # src_list.append(dic)
            item = ImageproItem()
            item['src'] = src
            item['img_name'] = img_name+'.jpg'
            yield item

        # print(len(src_list))
        # print(src_list)

