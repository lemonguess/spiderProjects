from requests_html import HTMLSession
import json
import re
import requests

'''
分析：响应内容还是在ajax里面，为post请求
'''
def homepage():
    session = HTMLSession()
    url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    response = session.get(url = url,headers=headers)
    XSRF_TOKEN = 'XSRF-TOKEN=' + response.cookies['XSRF-TOKEN']
    szxx_session = 'szxx_session=' + response.cookies['szxx_session']
    cookies = XSRF_TOKEN+'; '+szxx_session
    CSRF=re.findall("var _CSRF = '(.*?)';",response.text)[0]
    #print(CSRF)
    #print(cookies)
    return cookies,CSRF

def getdetails(Cookie,X_CSRF_TOKEN):

    s = HTMLSession()
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept - Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content - Length': '32',
    'Content - Type': 'application/x-www-form-urlencoded',
    'Host': 'www.zjmazhang.gov.cn',
    'Origin': 'http://www.jiedong.gov.cn',
    'Referer': 'http://www.jiedong.gov.cn/hdjlpt/published?via=pc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Cookie': Cookie,
    'X-CSRF-TOKEN': X_CSRF_TOKEN
    }

    # data1=json.dumps({
    #     'offset': 0,
    #     'limit': 20,
    #     'site_id': 759010
    # })
    # print(type(data1),data1)
    data2 = {
        'offset': 0,
        'limit': 20,
        'site_id': 759010
    }
    start_url = 'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList'
    response = s.post(url = start_url,
                    headers=headers,
                    data=data2)
    response.encoding='utf-8'
    #print(response.headers)
    print(response.text)


if __name__ == '__main__':
    #homepage()
    Cookie,X_CSRF_TOKEN=homepage()
    print(type(Cookie),Cookie)
    print(type(X_CSRF_TOKEN),X_CSRF_TOKEN)
    getdetails(Cookie,X_CSRF_TOKEN)