#coding=utf-8
from selenium import webdriver
from PIL import Image
from time import sleep
from lxml import etree
from Basic.Shibie import shibie
from selenium.webdriver import ActionChains

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')

bro.get('https://kyfw.12306.cn/otn/resources/login.html')
bro.maximize_window()


a_tag = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
a_tag.click()

userName_tag = bro.find_element_by_xpath('//*[@id="J-userName"]')
password_tag = bro.find_element_by_xpath('//*[@id="J-password"]')
userName_tag.send_keys('18203220212')
password_tag.send_keys('lxc13355506+')

#验证码图片进行捕获(裁剪）

bro.save_screenshot('main.png')
#定位到了验证码图片对应的标签
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location#验证码图片基于当前整张页面的左上角的坐标
size = code_img_ele.size #验证码图片的长和宽
print(location,size)
x1 = location['x']
y1 = location['y']
x2 = location['x'] + size['width']
y2 = location['y'] + size['height']
#裁剪的矩形区域(左下角和右上角两点的坐标)
# rangle = (x1+100,y1+70,x2+200,y2+110)
rangle = (x1+235,y1+70,x2*1.25,y2*1.25)
i = Image.open('main.png')#打开本地的图片
frame = i.crop(rangle)#对图片进行截取
frame.save('code.png')#将图片保存

#调用打码平台的示例程序进行识别
result = shibie('code.png',9004)
print(result)
print(shibie('code.png',9004))
#
# all_list = []#存储即将被电机的点的坐标
# if '|' in result:
#     list_1 = result.split('|')
#     count_1 = len(list_1)
#     for i in range(count_1):
#         xy_list = []
#         x = int(list_1[i].split(',')[0])
#         y = int(list_1[i].split(',')[1])
#         xy_list.append(x)
#         xy_list.append(y)
#         all_list.append(xy_list)
# else:
#     xy_list = []
#     x = int(result.split(',')[0])
#     y = int(result.split(',')[1])
#     xy_list.append(x)
#     xy_list.append(y)
#     all_list.append(xy_list)
# print(all_list)
#
# #遍历列表，使用动作链对每一个列表对应元素进行点击操作
# for l in all_list:
#     x=l[0]
#     y=l[1]
#     print(x,y)
#     ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
#



# tree = etree.HTML(bro.page_source)
# img_src=tree.xpath('//*[@id="J-loginImg"]/@src')[0]
# img_data = requests.get(url = img_src,headers = headers).content
# with open('./12306.jpg','wb') as fp:
#     fp.write(img_data)
# img_data = requests.get(url = img_src,headers = headers)


