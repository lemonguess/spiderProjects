#coding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class QiubaiproPipeline:
    fp = None
    #重写父类方法（生命周期方法）：该方法只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始爬虫...')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    #专门用来处理item类型对象
    #该方法可以接收爬虫文件提交过来的item对象
    #该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author+':'+content+'\n')


        return item #就会传递给下一个即将被执行的管道类
    def close_spider(self,spider):  #重写父类方法（生命周期方法）：该方法只在结束爬虫的时候调用一次
        print('结束爬虫！')
        self.fp.close()

class mysqlPipelines(object):

    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    passwd='qwe123',
                                    db='qiubai',
                                    charset='utf8')

    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            sql = f'INSERT INTO `qiubai` (`author`,`content`) VALUES ("{item["author"]}","{item["content"]}")'
            self.cursor.execute(sql)

        except Exception as e:
            print(e)
            self.conn.rollback() #出现异常，进行事务回滚
            with open('Error_log.txt','a+',encoding='utf-8') as fp:#将错误日志进行存储
                fp.write(sql+'\n')
        else:
            self.conn.commit() #没有问题，事务提交
            print('执行成功')
        return item #提交给下一个管道
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

#爬虫文件提交的item类型的对象，最终会提交给哪一个管道类？
    #先执行的管道类