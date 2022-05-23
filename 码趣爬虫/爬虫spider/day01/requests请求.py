import requests

"""
    requests 
    http://httpbin.org/get
    origin ip  
    user-agent  标识 
    accept 希望接收的数据类型
    args 参数
    get 传参  urlib3
        1. params
        2. 第一个加问号第二个以后是& 
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
word = {
    "name": "jingluo"
}
# response = requests.get(url="http://httpbin.org/get", headers=headers, params={"age": "18"})  # get请求
# response = requests.get(url="http://httpbin.org/get?sex=man&name=jingluo", headers=headers)  # get请求
# 虽然没问题 不建议这么干 不安全
# response = requests.post(url="http://httpbin.org/post", headers=headers,data=word)  # post请求
# response = requests.put(url="http://httpbin.org/put", headers=headers)  # put 接口
response = requests.head(url="http://httpbin.org/head", headers=headers)  # 没有数据

print(response.text)
