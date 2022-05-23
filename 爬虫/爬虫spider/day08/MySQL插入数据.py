import pymysql
import asyncio

"""
    insert into student (name,age) values ()
"""
host = "localhost"
port = 3307
db = "jingluo"
user = "admin"
password = "qwe123"
conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
cursor = conn.cursor()
cursor.execute("insert into student (id,name,age) values (5,'北斗','250');")
conn.commit() # 确认提交
cursor.close()
conn.close()