# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JobsproPipeline:
    fp = None
    #重写父类方法（生命周期方法）：该方法只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始写入...')
        with open('./BOSS_SpiderJobs.csv','a',encoding='utf-8') as self.fp:
            self.fp.write('职位名称,工作地点,薪资水平,要求年限,公司名称,福利待遇\n')

    def process_item(self, item, spider):
        job = item['job']
        place=item['place']
        salary=item['salary']
        year=item['year']
        c_name=item['c_name']
        fuli=item['fuli']
        with open('./BOSS_SpiderJobs.csv', 'a', encoding='utf-8') as self.fp:
            self.fp.write(f'{job},{place},{salary},{year},{c_name},{fuli}\n')
        return item
