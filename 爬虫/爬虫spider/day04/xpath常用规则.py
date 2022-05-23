"""
pip install lxml
lxml是解析器 主要功能是解析和提取HTML和xml的数据

 // 不管位置 匹配符合条件的
 / 获取子元素
 . 选取当前节点
 .. 选取当前节点的父节点
 @选取属性 
 * 匹配任何
"""

from lxml import etree

str1 = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html" text="shadjfhjisdf">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li aaa="鲸落" class="item-0"><a class="test" href="link5.html">fifth item</a></li>
     </ul>
</div>

"""
# 转成HTML
tree = etree.HTML(str1)

print(tree.xpath("//li"))  # 获取所有li
print(tree.xpath('//li/@class'))  # 所有li标签中的class属性值
print(tree.xpath('//li/@aaa'))  # 所有li标签中的aaa属性值

print(tree.xpath('//li/a'))
print(tree.xpath('//li/a[@href="link1.html"]'))  # href 标签属性值是link1的节点
print(tree.xpath('//li//span'))
print(tree.xpath('//li/a/@class'))  # ['test']
print(tree.xpath('//li/a//@class'))  # ['bold', 'test']
print(tree.xpath('//li[last()]/a/@href'))  # ['link5.html']   获取最后一个
print(tree.xpath('//li[last()-1]/a/@href'))  # ['link4.html']   获取倒数第二
print(tree.xpath('//li[1]/a/@href'))  # ['link1.html']  xpath中 索引是从1开始的
print(tree.xpath('//li[1]/a/text()'))  # ['first item'] text()取出内容

result = tree.xpath('//li[1]/a')
print(result[0].text)

print(tree.xpath('//*[@class="bold"]')[0].tag) # tag 获取标签
