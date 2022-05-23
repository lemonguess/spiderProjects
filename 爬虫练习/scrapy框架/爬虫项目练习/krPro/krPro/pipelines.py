# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
logger = logging.getLogger(__name__)
import os
class KrproPipeline:

    fp = None

    Title = None

    def process_item(self, item, spider):
        # logging.warning(item)
        mkdir_path = f'../文章/{spider.searchWord}相关文章'
        # print(mkdir_path)
        if os.path.exists(mkdir_path):
            pass
        else:
            os.makedirs(mkdir_path)
        # print('开始爬虫...')
        self.fp = open(f'{mkdir_path}/{item["Title"]}.txt','w',encoding='utf-8')
        # print(f'{mkdir_path}/{item["Title"]}.txt')
        self.fp.write(item['content'])
        self.Title = item['Title']
        return item
    def close_spider(self,spider):  #重写父类方法（生命周期方法）：该方法只在结束爬虫的时候调用一次
        print(f'《{self.Title}》 - 爬取成功')
        self.fp.close()



