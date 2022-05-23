from requests_html import HTMLSession
from bs4 import BeautifulSoup

"""
    
"""
session = HTMLSession()
url = 'https://www.bilibili.com/v/popular/rank/bangumi'
response = session.get(url=url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
name = []  # 标题
bfl = []  # 播放量
pl = []  # 评论
xh = []  # 喜欢
df = [] # 得分
for a in soup.select('div.info>a'):
    name.append(a.text)
print(name)
for i in soup.select('div.detail>span:nth-child(1)'):
    bfl.append(i.text.strip())
print(bfl)
for j in soup.select('div.detail>span:nth-child(2)'):
    pl.append(j.text.strip())
print(pl)
for x in soup.select('div.detail>span:nth-child(3)'):
    xh.append(x.text.strip())
print(xh)
for d in soup.select('div.pts>div'):
    df.append(d.text.strip())
print(df)