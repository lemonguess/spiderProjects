import pymongo
client = pymongo.MongoClient()#与MongoDB产生连接
db = client['name']#指定操作的数据库
stu = db['name']#指定操作的集合

stu.insert({'name':'moran','age':26})
stu.insert_many([{'name':'beidou','age':18},{'name':'yige','age':24}])