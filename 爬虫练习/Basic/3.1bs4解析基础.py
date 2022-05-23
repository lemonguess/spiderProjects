from bs4 import BeautifulSoup

#将本地的html文档中的数据加载到该对象中
fp = open('./huazhuangpin.html','r',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')
#soup.tagName()：返回的是文档中第一次出现的tagName标签
#print(soup.div)
#soup.find():
# print(soup.find('div'))#find('tagName'):等同于soup.div
# print(soup.find('div',class_ = "hzblist"))
# print(soup.find_all('div',class_ = "hzblist"))
#soup.select
a=soup.select('.hzbscbox > .hzbscin >  .hzbtabs > span')
len(a)
print(a)
