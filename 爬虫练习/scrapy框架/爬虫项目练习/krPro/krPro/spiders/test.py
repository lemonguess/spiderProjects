'''
param: {searchType: "article", searchWord: "奥运会", sort: "date", pageSize: 20, pageEvent: 1,…}
pageCallback: "eyJmaXJzdElkIjoxMzI3MDUzMzA0NzE1NTIxLCJsYXN0SWQiOjEzMjQyNTkzMTU1NTQzMTAsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzI5NDgzMTAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcxNjg0NDA0ODl9"
pageEvent: 1
pageSize: 20
platformId: 2
searchType: "article"
searchWord: "奥运会"
siteId: 1
sort: "date"
partner_id: "web"
timestamp: 1627420006194
==================================
sajssdk_2015_cross_new_user=1;
sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ae9c9aef2324-01f42d34760433-4373266-1327104-17ae9c9aef34%22%2C%22%24device_id%22%3A%2217ae9c9aef2324-01f42d34760433-4373266-1327104-17ae9c9aef34%22%2C%22props%22%3A%7B%7D%7D;
Hm_lvt_1684191ccae0314c6254306a8333d090=1627419947;
Hm_lpvt_1684191ccae0314c6254306a8333d090=1627419947;
Hm_lvt_713123c60a0e86982326bae1a51083e1=1627419947;
Hm_lpvt_713123c60a0e86982326bae1a51083e1=1627419947;
acw_tc=2760825616274199646618957eb559e0dca7417040440aa36bcfb880c5ae06
==============================================
pageCallback= "eyJmaXJzdElkIjoxMzI4ODQ1Nzg2ODQxNzM2LCJsYXN0SWQiOjEzMjc0NTM1NTM5MjQwOTcsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzM4NjYxMjAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcyOTc1MTUwMDB9"
              "eyJmaXJzdElkIjoxMzI4ODQ1Nzg2ODQxNzM2LCJsYXN0SWQiOjEzMjc0NTM1NTM5MjQwOTcsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzM4NjYxMjAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcyOTc1MTUwMDB9"
              "eyJmaXJzdElkIjoxMzI4ODQ1Nzg2ODQxNzM2LCJsYXN0SWQiOjEzMjc0NTM1NTM5MjQwOTcsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzM4NjYxMjAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcyOTc1MTUwMDB9"
'''
from requests_html import HTMLSession
import requests
import time
def kr():
    import json
    url = 'https://gateway.36kr.com/api/mis/nav/search/resultbytype'
    Request_Payload = {"param": {
        "pageCallback": "eyJmaXJzdElkIjoxMzI4ODQ1Nzg2ODQxNzM2LCJsYXN0SWQiOjEzMjc0NTM1NTM5MjQwOTcsImZpcnN0Q3JlYXRlVGltZSI6MTYyNzM4NjYxMjAwMCwibGFzdENyZWF0ZVRpbWUiOjE2MjcyOTc1MTUwMDB9",
        "pageEvent": 2,
        "pageSize": 2,
        "platformId": 1,
        "searchType": "article",
        "searchWord": "奥运会",
        "siteId": 1,
        "sort": "date"},
     "partner_id": "web",
     "timestamp": "1627469455770"
     }
    headers = {
    'authority': 'gateway.36kr.com',
    'method': 'POST',
    'path': '/api/mis/nav/search/resultbytype',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    #'content-length': '346',
    #'cookie': 'Hm_lvt_1684191ccae0314c6254306a8333d090=1627469447; Hm_lpvt_1684191ccae0314c6254306a8333d090=1627469447; Hm_lvt_713123c60a0e86982326bae1a51083e1=1627469447; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1627469447; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217aecbcffa51fe-0d9880bc07d69d-4373266-1327104-17aecbcffa6186%22%2C%22%24device_id%22%3A%2217aecbcffa51fe-0d9880bc07d69d-4373266-1327104-17aecbcffa6186%22%2C%22props%22%3A%7B%7D%7D',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'origin': 'https://36kr.com',
    'pragma':'no-cache',
    'referer': 'https://36kr.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site'

    }
    response = requests.post(url=url,json=Request_Payload,headers = headers)
    with open('kr.json','w',encoding='utf-8') as fp:
        fp.write(response.text)
    itemList = json.loads(response.text)["data"]["itemList"]
    print(itemList,type(itemList))
def ECP_SGCC():
    data = {
        'firstPageMenuId': "2018032700291334",
        'index': '3',
        'key': "",
        'orgId': "",
        'orgName': "",
        'purOrgCode': "",
        'purOrgStatus': "",
        'purType': "",
        'size': '20'
    }
    UA = {
        'Cookie': 'BIGipServerpool_ecp2_0=!d9E+BWMAhhxtQaawBfj7kQDFO4jKCwMgUAgw3PgFN7mSFPDzHVMUiS3RVT0plE1tz/qGJW7ptSKRJg==; JSESSIONID=FE5E2205685EF99C5F7A9FBA6DEE005B',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    url = 'https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/noteList'
    response = requests.post(url=url,json = data,headers = UA)
    print(response.json())

#ECP_SGCC()
# kr()
