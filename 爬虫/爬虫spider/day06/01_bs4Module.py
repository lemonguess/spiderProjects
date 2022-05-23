"""
    BeautifulSoup4 可以从HTML/xml提取数据的库
"""
from bs4 import BeautifulSoup
import  re
html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span>鲸落好帅</a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" aaa="abc" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<p>story</P>
"""

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
print(type(soup))

# print(soup.prettify())  # 格式化代码

print(soup.title)  # 完整的标签
print(soup.title.name)  # 标签

print(soup.a)  # 拿第一个
print(soup.a.attrs)  # 获取属性
print(soup.a.attrs['href'])
print(soup.a['href'])
print(soup.a.get('href'))
soup.a['href'] = "www.baidu.com"  # 修改
print(soup.a['href'])

# <a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span>鲸落好帅</a>
# string得到标签下的文本内容，只有在此标签下没有子标签，或者只有一个子标签的情况下才能返回其中的内容，否则返回的是None;
# get_text()可以获得一个标签中的所有文本内容，包括子孙节点的内容，这是最常用的方法
print(soup.a.string)
print(soup.a.text)
print(soup.a.get_text())

# for i in soup.find_all('a'):
#     print(i['href'])
#     print(i.text)  # 鲸落好帅


print(soup.find_all('a', class_="sister")) # class是关键字
print(soup.find_all('a', id="link3"))
print(soup.find_all('a',aaa="abc", id="link3")) # 组合使用


print(soup.find_all(text='story'))
print(soup.find_all(text=re.compile('.*?story.*?')))