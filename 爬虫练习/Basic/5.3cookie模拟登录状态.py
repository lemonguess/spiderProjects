#coding=utf-8
import requests
from lxml import etree
from Shibie import shibie

url = "https://so.gushiwen.cn/user/login.aspx"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = requests.get(url=url,headers = headers).text
#print(requests.get(url).encoding)
tree = etree.HTML(page_text)
img_src ='https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url = img_src,headers = headers).content
#保存验证码图片
with open('./验证码.jpg','wb') as fp:
    fp.write(img_data)

#调用打码平台的示例程序进行识别
an = shibie('验证码.jpg',1902)
print('平台验证码：',an)

#登录网站
log_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
param = {

'from':'http://so.gushiwen.cn/user/collect.aspx',
'email':'137790410@qq.com',
'pwd':'lxc13355506',
'code':an,
'denglu':'登录',
}
#session
s = requests.Session()
response = s.post(url = log_url,data = param,headers = headers)
if response.status_code == 200:
    print('登录成功!!')
else :
    print('登录失败，请重新操作!')
repage_text = s.get(url = 'https://so.gushiwen.cn/user/collect.aspx',headers = headers)

with open('./我的古诗文.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
