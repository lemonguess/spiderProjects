from MyMongoDB import MyMongoDB
class TaocheproPipeline:

    monggoDB = None
    def open_spider(self,spider):
        if spider.name=='taoche':
            print('开始爬取：')
            self.monggoDB = MyMongoDB('taoche','car')# MyMongoDB('库','集合')，实例化一个MongoDB的集合
    def process_item(self, item, spider):
        # print(item)
        if spider.name =='taoche':
            self.monggoDB.insert(dict(item))#mongoDB插入字典数据
        return item

    def close_spider(selfself,spider):
        if spider.name=='taoche':
            print('结束爬取！')

# from MyMongoDB import MyMongoDB
# class TaocheproPipeline:
#
#     def process_item(self, item, spider):
#         print(item)
#         # if spider.name =='taoche':
#         #     self.monggoDB.insert(dict(item))#mongoDB插入字典数据
#         return item

