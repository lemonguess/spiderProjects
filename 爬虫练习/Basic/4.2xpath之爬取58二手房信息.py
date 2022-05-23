from lxml import etree
import requests

#爬取页面源码数据
url = "https://nj.58.com/ershoufang/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
#数据解析
tree = etree.HTML(page_text)
list1 = tree.xpath('//section[@class="list"][1]/div')

for li in list1:
    title = li.xpath('.//div[@class="property-content-title"]/h3/test()')[0]
    print(title)