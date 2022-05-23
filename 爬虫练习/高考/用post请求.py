import requests

url = 'https://api.eol.cn/gkcx/api/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
# Ip_url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=1b12205d2f5f4b13a9c24607b98713af&orderno=YZ20216285668MAuVdq&returnType=2&count=10'
# ip_pool = requests.get('')

for page in range(83,144):
    param = {
    "access_token":"" ,
    "admissions": "",
    "central": "",
    "department": "",
    "dual_class":"",
    "f211": "",
    "f985": "",
    "is_doublehigh": "",
    "is_dual_class": "",
    "keyword": "",
    "nature": "",
    "page": page,
    "province_id": "",
    "e": "",
    "request_type": "1",
    "school_type": "",
    "signsafranktype": "",
    "size": "20",
    "sort": "view_total",
    "top_school_id": "[659]",
    "type": "",
    "uri": "apidata/api/gk/school/lists"
    }
    response = requests.post(url=url, params=param, headers=headers)
    #data = response.text
    with open(f'./urls/school_{page}.json', 'w', encoding='utf-8') as fu:
        fu.write(response.text)
    fu.close()

    print(f"============爬取进度：{page}/143==============")