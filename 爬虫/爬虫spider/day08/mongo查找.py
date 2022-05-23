from pymongo import MongoClient

conn = MongoClient('localhost', 10086)
db = conn.spider  # 如果没有这个数据库就创建
my_set = db.words  # 如果没有这个表（集合）就创建

print(my_set.find())
for data in my_set.find():
    print(data)
    print(data['age'])