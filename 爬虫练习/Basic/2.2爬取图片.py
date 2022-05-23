import requests
url = 'https://pic.qiushibaike.com/system/pictures/12437/124370845/medium/4LVWKEKJ4DXNX3P2.jpg'
'''
text:返回字符串数据
content：返回二进制数据
json:返回对象类型数据
'''
img_data = requests.get(url=url).content
with open('./qiutu.jpg','wb') as fp:
    fp.write(img_data)