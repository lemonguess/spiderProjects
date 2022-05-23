# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class ImagesPipeline(object):
#     def process_item(self, item, spider):
#         return item


#导入管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imagsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        '''
        基于一个媒体资源进行请求发送
        可以根据图片地址进行图片数据的请求
        '''
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        '''
        指定图片存储的路径
        :param request:
        :param response:
        :param info:
        :param item:
        :return:
        '''
        # imgName='dghfghfg.jpg'
        imgName=item['img_name']
        return imgName

    def item_completed(self, results, item, info):
        #返回给下一个即将被执行的管道类
        return item
