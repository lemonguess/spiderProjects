import pymysql

conn_win = pymysql.connect(host='localhost',
                       port=3306,
                       db='qiubai',
                       user = 'root',
                       password='qwe123')

cursor = conn_win.cursor()
cursor.execute("insert into student (name,age) values ('Jack',39);")
conn_win.commit()#确认提交
cursor.close()
conn_win.close()

conn_linux = pymysql.connect(host='localhost',
                       port=3307,
                       db='test',
                       user = 'admin',
                       password='qwe123')
cursor = conn_linux.cursor()
cursor.execute("insert into student (name,age) values ('Jack',39);")
conn_linux.commit()#确认提交
cursor.close()
conn_linux.close()