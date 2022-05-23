from requests_html import HTMLSession
import requests


session = HTMLSession() # 实例化
url = "https://www.baidu.com/"
response = session.get(url=url) # 默认携带了UA
response2 = requests.get(url=url)

print(response.text)
print("----------------鲸落-----------")
print(response2.text)