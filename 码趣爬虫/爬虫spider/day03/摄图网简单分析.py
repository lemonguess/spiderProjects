from requests_html import HTMLSession

session = HTMLSession()
url="https://699pic.com/tupian/4204557.html"
response = session.get(url=url)
# print(response.html.xpath('//div[@class="list"]/a/@href'))
# url_list =response.html.xpath('//div[@class="list"]/a/@href')
# for  url_i in url_list:
#     print(url_i)
# print(response.html.links) # 获取页面所有链接
print(response.html.absolute_links) # 获取页面所有链接 自动转换路径 去重
# for titile in response.html.xpath('//div[@class="list"]/a/@title'):
    # print(titile)