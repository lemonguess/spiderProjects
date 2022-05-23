#使用python操作MySQL
import pymysql
db_config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'admin',
    'password' : 'qwe123',
    'db' : 'test',
    'charset' : 'utf8'
}
conn = pymysql.connect()
cur = conn.cursor()#获得游标对象（SQL语句的执行都是依赖游标进行）
sql = 'insert into test(name,age,phone) values("金刚葫芦娃",23,"18232105436"),("曹尼玛",24,"1800000000")'
res = cur.excute(sql)#通过游标执行SQL语句 pymysql进行操作时会默认开启事务
print(res)

conn.commit() #提交
cur.close() #关闭游标
conn.close() #关闭链接