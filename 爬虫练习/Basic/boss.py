import requests
from parsel import Selector
from lxml import etree
import re
'''
场景：刷单 点赞 投票 爬虫（反爬虫）
1.IP电脑没有换IP
2.Cookie电脑没有换Cookie（登录信息 账号）
'''
import dailiIP
from time import sleep
ip_list=[]
#函数的定义
def getOnePageHTml(page):
    '''
    获取一页的数据 就是获取第几页的数据
    ：return：HTML网页
    :return:
    '''
    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    return response.text



#解析HTML获得数据
def parseOneHTMLPage(text):
    #初始化需要从html中选择的内容
    selectors = Selector(text=text)
    selectors=selectors.xpath('//*[@id="list"]/table//tr')[1:]
    i = 1
    for selector in selectors:
        ip = selector.xpath('./td[1]/test()').get()
        port = selector.xpath('./td[2]/test()').get()

        print(ip,port,i)
        i +=1
        item=f'{ip}:{port}'
        if 'None' not in item:
            pipelinesCSV(item)



#保存数据
def pipelinesCSV(item):
    with open('kuaidaili.csv','a',encoding='utf-8') as fp:
        fp.write(item+ '\n') #item应该是一个字符串

#运行程序
def main():
    for page in range(1,100):
        text = getOnePageHTml(page)
        parseOneHTMLPage(text)
        sleep(0.5)
if __name__ == '__main__':
    main()




