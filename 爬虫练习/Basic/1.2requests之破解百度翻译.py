import requests
import json
#1.指定url
post_url = 'https://fanyi.baidu.com/sug'
#2.进行UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#3.post请求参数处理（同get请求一致）
word = input('请输入要查询的单词：')
data = {
    'kw':word
}
#4.请求发送
response = requests.post(url=post_url,data=data,headers=headers)
#5.获取响应数据：json()方法返回的是obj(对象)；
'''如果确认响应数据 是json类型的，才可以使用json()
Cache-Control: no-cache, private
Content-Encoding: gzip
Content-Length: 56
Content-Type: application/json
Date: Thu, 27 May 2021 20:10:09 GMT
Server: Apache
Tracecode: 06093780840615616522052804
Vary: Accept-Encoding'''
print(type(response))
dic_obj = response.json()
print(type(dic_obj))

#6.持久化存储
# filename =word+'.json'
# fp = open(filename,'w',encoding='utf-8')
# json.dump(dic_obj,fp=fp,ensure_ascii=False)
#
# print('over!!')