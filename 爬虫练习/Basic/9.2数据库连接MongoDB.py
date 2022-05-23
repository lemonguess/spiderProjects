"""
    MongoDB是一个基于分布式文件存储的数据库。和MySQL不同，MongoDB是一个介于关系数据库和非关系数据库之间的产品，属于非关系型数据库。
    MongoDB功能比较丰富，非常适合在爬虫开发中用作大规模数据的存储
    mongodb ubuntu下安装以及开启远程访问

1. sudo vi /etc/mongodb.conf
    将 bind_ip 127.0.0.1  修改为 bind_ip 0.0.0.0
2. /etc/init.d/mongodb restart   重启服务
"""
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.spider  # 如果没有这个数据库"spider"就创建
my_set = db.words  # 如果没有这个表（集合）"words"就创建

data = [{'name': "翻车现场", 'age': [1,2,3,4]}]
my_set.insert(data)

#MongoDB查找
for data in my_set.find():
    print(data)
    print(data['age'])