from requests_html import HTMLSession
import requests
import re
import random
import time
import json
import jsonpath

session = HTMLSession()
def Homepage():
    UA = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    start_url = 'http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact'
    response = session.get(url = start_url,headers = UA)
    page_text = response.text
    signature = re.findall('__signature = "(.*?)";',page_text)[0]
    #var __signature = "c352621626525349952";
    cookies = 'ICITYSession='+response.cookies['ICITYSession']
    return signature,cookies
def getURL():
    '''
    s: c118841626525606851(signature)
    t: 7798_c66666_1626525604000

var key = "";
var keyIndex = -1;
for(var i=0;i<6;i++){
    var c=sig.charAt(keyIndex+1);
    key +=c;
    keyIndex = chars.indexOf(c);
    if(keyIndex<0 || keyIndex>=sig.length){
        keyIndex = i;
    '''
    key = ""
    chars = "0123456789abcdef"
    # print(type(Homepage()),Homepage())
    # print(type(Homepage()[0]),Homepage()[0])
    signature = Homepage()[0]
    '''
    1. http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=d728831626528690100&t=9690_d95128_1626528684000
    2. http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s=ea82321626528728595&t=9317_e86666_1626528723000
    '''
    keyIndex = -1
    for i in range(0,6):

        c = signature[keyIndex+1]
        key +=c
        keyIndex = chars.index(c)
        if keyIndex<0 and keyIndex>=len(signature):
            keyIndex = i
    timestamp = str(int(random.random() * (9999 - 1000 + 1)) + 1000)+f"+{key}+"+str(int(time.time()))+"000"
    t = timestamp
    t = t.replace('+','_')
    url = f'http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList?s={signature}&t={t}'
    # print(t)
    # print('url:',url)
    return url
def Detailpage(url,cookies):
    url = url

    headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '47',
    'Content-Type':'application/json',
    'Cookie':cookies,
    'Host':'zwfw.san-he.gov.cn',
    'Origin':'http://zwfw.san-he.gov.cn',
    'Referer':'http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    }
    UA = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    data = {
            'start': 0,
            'limit': 7,
            'TYPE@=': "2",
            'OPEN@=': "1"
            }
    data = json.dumps(data)
    response = requests.post(url = url,headers=headers,data = data)
    response.encoding = 'utf-8'
    data = str(response.json())
    data = data.replace("'",'"')
    #data = jsonpath.jsonpath(data,'$data')
    print(data)


if __name__ == '__main__':
    cookies = Homepage()[1]
    url = getURL()
    print('url:',url)
    print('cookies:', cookies)
    Detailpage(url,cookies)
