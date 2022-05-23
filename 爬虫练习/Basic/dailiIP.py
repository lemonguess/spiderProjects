import requests
from parsel import Selector
from lxml import etree
import re

'''
场景：刷单 点赞 投票 爬虫（反爬虫）
1.IP电脑没有换IP
2.Cookie电脑没有换Cookie（登录信息 账号）
'''
from time import sleep
#函数的定义
def getOnePageHTml(page):
    '''
    获取一页的数据 就是获取第几页的数据
    ：return：HTML网页
    :return:
    '''
    url = f'http://www.kxdaili.com/dailiip/1/{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    return page_text

#解析HTML获得数据
def parseOneHTMLPage(text):
    #初始化需要从html中选择的内容
    selectors = Selector(text=text)
    selectors=selectors.xpath('//div[@class="hot-product-content"]/table//tr')[1:]
    oip_list=[]
    for selector in selectors:
        ip = selector.xpath('./td[1]/test()').get()
        port = selector.xpath('./td[2]/test()').get()
        item=f'{ip}:{port}'
        print(f'HTTP:{item}')
        oip_list.append(item)
        if 'None' not in item:
            pipelinesCSV(item)

        CheckIP(item)

#检查IP是否可用
def CheckIP(item):
    proxy = {
        'http': item
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        response = requests.get('https://www.baidu.com',headers=headers,proxies=proxy,timeout=0.1)
        if response.status_code==200:
            usefulIP_list.append(proxy)
    except Exception as e :
        print(e)
    finally:
        print('当前ip',item,'检测通过')


#保存数据
def pipelinesCSV(item):
    with open('kxdaili.csv','a',encoding='utf-8') as fp:
        fp.write(item+ '\n') #item应该是一个字符串

#运行程序
def main():
    global usefulIP_list
    usefulIP_list=[]
    for page in range(1,3):
        text = getOnePageHTml(page)
        parseOneHTMLPage(text)
        sleep(0.5)
        print(f'=================第{page}页爬取成功=================')
    return usefulIP_list

if __name__ == '__main__':
    main()




