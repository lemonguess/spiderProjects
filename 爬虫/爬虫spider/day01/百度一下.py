import requests

url = "https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=url, headers=headers)
# print(response.text) # 返回的是响应内容
print(response.url)  # 查看url
print(response.request.url)  # 查看url
print(response.encoding)  # 编码格式
print(response.status_code)  # 响应码
# print(response.content)  # 返回二进制数据
print(response.headers)
print(response.request.headers)
print(response.request)
cook=response.cookies #cookieJar 对象
print(requests.utils.dict_from_cookiejar(cook)) # 转字典



