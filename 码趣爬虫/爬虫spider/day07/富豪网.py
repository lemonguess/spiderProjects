"""
    爬虫四步
    1. 确定要爬取的网站
    2. 爬
    3. 取
    4. 存
"""
from requests_html import HTMLSession
import re
import csv

session = HTMLSession()

url = f"https://www.phb123.com/renwu/fuhao/shishi_.html"
# for page in range(1,16):
#     response = session.get(url=url)
response = session.get(url=url)
# print(len(response.html.xpath('//table[@class="rank-table"]//tr/td[2]/a/p/text()')))
# print(len(response.html.xpath('//table[@class="rank-table"]//tr/td[3]/text()')))
# print(len(response.html.xpath('//table[@class="rank-table"]//tr/td[4]/text()')))
# print(len(response.html.xpath('//table[@class="rank-table"]//tr/td[5]/a/text()')))
# for tr in response.html.xpath('//table[@class="rank-table"]//tr')[1:]:
#     source = ["无"]
#     source_xpath = tr.xpath('//td[4]/text()')
#     if source_xpath==[]:
#         source_xpath = source
#     print(source_xpath)
datas = []
for page in range(1, 16):
    url = f"https://www.phb123.com/renwu/fuhao/shishi_{page}.html"
    response = session.get(url=url)
    data_list = re.findall('<td.*?"xh".*?>(.*?)<.*?<p>(.*?)</p>.*?<td>(.*?)</td>.*?<td>(.*?)<.*?title="(.*?)"',
                           response.text,
                           re.S)
    datas += data_list
    # print(data_list)
print(datas)

headers = ('世界排名', '名字', '财富(10亿美元)', '财富来源', "国家/地区")
with open("富豪榜.csv", "w", encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(datas)
"""
世界排名	名字			
https://www.phb123.com/renwu/fuhao/shishi_1.html
https://www.phb123.com/renwu/fuhao/shishi_2.html
https://www.phb123.com/renwu/fuhao/shishi_3.html
"""
