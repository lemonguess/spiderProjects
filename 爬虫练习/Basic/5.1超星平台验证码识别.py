#coding=utf-8
import requests
from lxml import etree
from Shibie import shibie
from bbb import IMG
import re

url = "http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = requests.get(url=url,headers = headers).text
#print(page_text)

tree = etree.HTML(page_text)
a = tree.xpath('//*[@id="numVerCode"]')
#print(a)
img_src ='http://passport2.chaoxing.com' + '/num/code?1622758448270'

print(img_src)
img_data = requests.get(url = img_src,headers = headers).content
#保存验证码图片
with open('./y.jpg','wb') as fp:
    fp.write(img_data)

#调用打码平台的示例程序进行识别
an = shibie('y.jpg',1902)
print(an)



