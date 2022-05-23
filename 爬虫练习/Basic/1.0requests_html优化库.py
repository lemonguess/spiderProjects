from requests_html import HTMLSession
import requests

session = HTMLSession()#实例化
url = "https://www.baidu.com/"

response = session.get(url=url)#默认携带了UA
response2 = session.get(url=url)

print(response)
#获取HTML页面所有的链接
print(response.html.links)
print(response.html.absolute_links)
print('\n\n\n\n========================================\n\n\n\n')
print(response2)