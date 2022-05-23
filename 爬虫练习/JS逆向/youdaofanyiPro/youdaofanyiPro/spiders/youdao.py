import scrapy
from time import time
import random
from hashlib import md5

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',]
    def start_requests(self):
        # 获取查询单词
        word = input('请输入你要查询的单词:')
        # 获取当前时间戳
        lts = str(int(time() * 1000))
        # 获取salt
        salt = lts + str(random.randint(0, 9))
        # 获取sign
        sign = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        md = md5()  # 实例化——得到MD5加密对象
        md.update(sign.encode())  # 生成加密数据
        sign = md.hexdigest()
        post_data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': '679a714475741baa9769e4725c532bb7',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        # 将cookie转成字典类型
        cookies = 'OUTFOX_SEARCH_USER_ID=1370777476@2409:8920:400:46ac:a171:61b:7868:1c32; OUTFOX_SEARCH_USER_ID_NCOO=1092215250.8540661; UM_distinctid=179d34a1f154d-057d5ca47388f3-6701b35-144000-179d34a1f161e3; JSESSIONID=aaap-S9l5WclRfOMVkgQx; ___rl__test__cookies='+lts
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
        print(post_data)
        # 手动发送post请求
        yield scrapy.FormRequest(url = self.start_urls[0],
                                 headers={
            'Host': 'fanyi.youdao.com',
            'Origin': 'https://fanyi.youdao.com',
            'Referer': 'https://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        },
                                 formdata=post_data,
                                 callback=self.parse,
                                 cookies = cookies)
    def parse(self, response):
        print(response,response.text)
        #print(response,response.request.headers,response.request.method,response.text)
