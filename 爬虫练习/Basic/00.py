#coding=utf-8
import requests
import chardet
from bs4 import BeautifulSoup

import time
from lxml import etree
for i in range(260,300):
    # new_url=url+str(i)+".htm"
    url="http://news.whu.edu.cn/wdyw/{}.htm".format(i)


    headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }


    rasp=requests.get(url=url,headers=headers)
    # rasp.encode('utf-8')
    rasp.encoding = rasp.apparent_encoding
    rasp = rasp.text
    print(chardet.detect(str.encode(rasp)))
    # print(rasp)
# rasp=requests.get(url=url,headers=headers).test
# print(rasp)
##对页面进行分析
    html=etree.HTML(rasp)
    divs=html.xpath('//*[@id="page_main"]/div[3]/div/div[2]/div[1]/ul/li')
    del divs[0]
    for div in divs:
        title=div.xpath('./div[1]/a/test()')[0]  #类容以列表形象输出
        print(title)