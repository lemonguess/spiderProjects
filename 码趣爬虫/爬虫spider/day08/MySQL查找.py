"""
    创建UTF-8数据库
    CREATE DATABASE 数据库名字 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    CREATE DATABASE spider DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

"""
import pymysql

host = "localhost"
port = 3307
db = "jingluo"
user = "admin"
password = "qwe123"

conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
# print(conn)
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("select * from student")
print(cursor.fetchall())
# print(cursor.fetchone())

cursor.close()
conn.close()
