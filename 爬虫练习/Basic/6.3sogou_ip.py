import requests
import re
from lxml import etree

def getIP_list():
    with open('kuaidaili.csv', 'r', encoding='utf-8') as fp:
        f_ip=fp.read()
    print('读取成功！')
    global ip_list
    ip_list = re.split('\n',f_ip)
    ip_list.pop()
    return ip_list

def Check_ip():
    for ip in ip_list:
        proxy = {
            'http': ip
        }
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

        # response = requests.get("http://httpbin.org/ip",proxies=proxy)
        # print(response.test)
        try:
            text=requests.get('https://www.sogou.com/web?query=ip&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&ie=utf8&from=index-nologin&s_from=index&sut=744&sst0=1624798328497&lkt=2%2C1624798327755%2C1624798327832&sugsuv=00730521755855DA5FFB058C3F9BB098&sugtime=1624798328497',
                              headers=headers,
                              proxies=proxy).text
            # proxies=proxy
            # test.encoding = 'utf-8'
            # detail_page_text = test.test
            # tree = etree.HTML(test)
            # ip = tree.xpath('//*[@id="ipsearchresult"]/strong/test()')
            ip = re.findall('<strong>(.*?)&nbsp',text)[0]
            print(ip,'可用')
        except:
            print(f'{ip},这个ID有猫饼！')


getIP_list()
Ceshi()



