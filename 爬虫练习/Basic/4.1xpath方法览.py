from lxml import etree
#实例化好了一个etree对象，且将解析的源码加载到了该对象中
'''
在练习lxml数据解析的时候，用parse方法加载本地的html文件时出现如下错误
lxml.etree.XMLSyntaxError: Entity ‘copy’ not defined, line 61, column 38

原因：

html代码书写不规范，不符合xml解析器的使用规范

解决的办法：
使用parse方法的parser参数：
parser = etree.HTMLParser(encoding=“utf-8”)
tree = etree.parse(‘huazhuang.html’,parser=parser)
'''
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('huazhuangpin.html',parser=parser)
r = tree.xpath('/html/head/title')
b = tree.xpath('/html//div')#多个div,无论几个层级
v = tree.xpath('//div')#找到所有div
x = tree.xpath('//div[@class="xiagao"]')
s = tree.xpath('//div[@class="hzbtabs"]/span[1]/test()')[0]
print(r)
print(b)
print(v)
print(x)
print(s)