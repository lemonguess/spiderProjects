import pymongo

class MyMongoDB:
    def __init__(self,database,collection):
        #连接MongoDB
        self.cline = pymongo.MongoClient("mongodb://127.0.0.1:27017")#进入MongoDB软件
        self.db = self.cline[database]#切换数据库
        self.col = self.db[collection]#操作集合

    def insert(self,data,onlyOne=True):
        if not isinstance(onlyOne,bool):
            raise TypeError
        self.col.insert_one(data) if onlyOne else  self.col.insert_many(data)
    def find(self,query,onlyOne=True):
        if not isinstance(onlyOne,bool):
            raise TypeError
        self.col.find_one(query) if onlyOne else  self.col.find(query)
    def update(self,data,new_data,onlyOne=True):
        if not isinstance(onlyOne,bool):
            raise TypeError
        self.col.update_one(data,{'$set': new_data}) if onlyOne else  self.col.update_many(data,{'$set': new_data})
    def delete(self,data,onlyOne=True):
        if not isinstance(onlyOne,bool):
            raise TypeError
        self.col.delete_one(data) if onlyOne else  self.col.delete_many(data)