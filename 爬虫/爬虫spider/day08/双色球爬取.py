from requests_html import HTMLSession
import pymysql
from pymongo import MongoClient


class Spider:
    def __init__(self):
        self.url = "https://datachart.500.com/ssq/history/newinc/history.php?start=19000&end=21077"
        self.session = HTMLSession()
        conn = MongoClient('localhost', 10086)
        db = conn.spider  # 如果没有这个数据库就创建
        self.my_set = db.doubleball  # 如果没有这个表（集合）就创建

        host = "localhost"
        port = 3307
        db = "jingluo"
        user = "admin"
        password = "qwe123"
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
        self.cursor = self.conn.cursor()

    def parse(self):
        response = self.session.get(url=self.url)
        for tr in response.html.xpath('//tbody[@id="tdata"]/tr'):
            number = tr.xpath('//td[1]/text()')[0]
            red = tr.xpath(
                '//td[2]/text() | //td[3]/text() | //td[4]/text()| //td[5]/text()| //td[6]/text()| //td[7]/text()')
            blue = tr.xpath('//td[8]/text()')[0]
            pool = tr.xpath('//td[10]/text()')[0]
            first_price = tr.xpath('//td[11]/text() | //td[12]/text()')
            accessit = tr.xpath('//td[13]/text() | //td[14]/text()')
            Betting_amount = tr.xpath('//td[15]/text() ')[0]
            time = tr.xpath('//td[16]/text() ')[0]
            data = (number, red, blue, pool, first_price, accessit, Betting_amount, time)
            print(data)
            self.MongoDB(data)
            self.Mysql(data)

    def MongoDB(self, data):
        self.my_set.insert({
            "number": data[0],
            "red": data[1],
            "blue": data[2],
            "pool": data[3],
            "first_price": data[4],
            "accessit": data[5],
            "Betting_amount": data[6],
            "time": data[7],
        })

    def Mysql(self, data):
        self.cursor.execute("insert into doubleball values ('%s','%s','%s','%s','%s','%s','%s','%s');" % (
            data[0],
            "-".join(data[1]),
            data[2],
            data[3],
            "-".join(data[4]),
            "-".join(data[5]),
            data[6],
            data[7],
        ))
        self.conn.commit()

    def run(self):
        self.parse()
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
"""
https://datachart.500.com/ssq/history/newinc/history.php?start=19000&end=21077
"""
