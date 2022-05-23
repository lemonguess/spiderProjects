from requests_html import HTMLSession
from bs4 import BeautifulSoup


class Spider:
    def  __init__(self):
        self.session = HTMLSession()
        self.name = []  # 标题
        self.bfl = []  # 播放量
        self.pl = []  # 评论
        self.xh = []  # 喜欢
        self.df = []  # 得分

    def parse(self,response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.select('div.info>a'):
            self.name.append(a.text)
        print(self.name)
        for i in soup.select('div.detail>span:nth-child(1)'):
            self.bfl.append(i.text.strip())
        print(self.bfl)
        for j in soup.select('div.detail>span:nth-child(2)'):
            self.pl.append(j.text.strip())
        print(self.pl)
        for x in soup.select('div.detail>span:nth-child(3)'):
            self.xh.append(x.text.strip())
        print(self.xh)
        for d in soup.select('div.pts>div'):
            self.df.append(d.text.strip())
        print(self.df)

    def run(self):
        url = 'https://www.bilibili.com/v/popular/rank/bangumi'
        response = self.session.get(url=url)
        self.parse(response)

if __name__ == '__main__':
    spider = Spider()
    spider.run()