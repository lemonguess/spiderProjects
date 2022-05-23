import requests
import re
from selenium import webdriver
import boss

from time import sleep

def getIP_list():
    with open('kuaidaili.csv', 'r', encoding='utf-8') as fp:
        f_ip=fp.read()
    print('读取成功！')
    global ip_list
    ip_list = re.split('\n',f_ip)
    ip_list.pop()
    return ip_list

def getRespons():
    useful_list=[]
    i=1
    for ip in ip_list:
        proxy = {
            'http': ip
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        try:
            response = requests.get("http://httpbin.org/ip",headers=headers,proxies=proxy)
            print(f'{ip}响应有效，\nresponse：',response)
            print(i)
            with open('useful_ID.csv', 'a', encoding='utf-8') as fp:
                fp.write(ip+'\n')
        except:
            print(i,f'{ip},这个ID有猫饼！')
        i +=1

getIP_list()
getRespons()