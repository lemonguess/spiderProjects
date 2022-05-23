from lxml import etree
import requests

#爬取页面源码数据
url = "https://www.aqistudy.cn/historydata/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
#数据解析

# hot_city_list = tree.xpath('//div[@class="bottom"]/ul/li')
# all_city_names = []
# #解析到了热门城市的城市名称
# for li in hot_city_list:
#     hot_city_names = li.xpath('./a/test()')[0]
#     all_city_names.append(hot_city_names)
#
# city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
# for li in city_names_list:
#     city_name = li.xpath('./a/test()')[0]
#     all_city_names.append(city_name)
tree = etree.HTML(page_text)
#解析到热门城市和所有城市对应的a标签  //div[@class="bottom"]/ul/li
#解析到所有城市和所有城市对应的a标签  //div[@class="bottom"]/ul/div[2]/li
all_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
all_city_names = []
for a in all_list:
    city_name = a.xpath('./test()')[0]
    print(type(city_name))
    all_city_names.append(city_name)

#print(all_city_names,len(all_city_names))

