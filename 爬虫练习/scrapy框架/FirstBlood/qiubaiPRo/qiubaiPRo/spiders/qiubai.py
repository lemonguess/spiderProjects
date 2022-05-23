#coding=utf-8
import scrapy
from qiubaiPRo.items import QiubaiproItem
import logging
logger = logging.getLogger(__name__)

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     ##解析作者的名称+段子内容
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data = []#存储所有解析到的数据
    #     for div in div_list:
    #         #xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract()可以将Selector对象中data参数存储的字符串提取出来
    #         '''
    #         如果返回的列表只有一个元素，那么可以写成：
    #         author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/test()').extract_first()
    #         '''
    #         author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/test()')[0].extract()
    #         #列表调用了extract之后，则表示将列表中每一个Selector对象中的data对应的字符串提取了出来
    #         content = div.xpath('./a[1]/div/span//test()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        ##解析作者的名称+段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')

        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract()可以将Selector对象中data参数存储的字符串提取出来
            '''
            如果返回的列表只有一个元素，那么可以写成： 
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/test()').extract_first()
            '''
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/test()' )[0].extract()
            #列表调用了extract之后，则表示将列表中每一个Selector对象中的data对应的字符串提取了出来
            content = div.xpath('./a[1]/div/span//test()').extract()
            content = ''.join(content)
            content = content.replace('\n','')

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            logger.warning(item)
            #yield item#将item提交给管道
