from lxml import etree

tree = etree.parse("xpath2.html")
print(tree.xpath('//@code'))  # 匹配所有带有code属性的属性值
# 用于xpath写多个表达式 用| 连接
print(tree.xpath('//div[@id="testid"]/h2/text() | //li[@data]/text() | //div/h3/text()'))

""" child：选取当前节点的所有子元素 """
# child子节点定位
print(tree.xpath('//div[@id="testid"]/child::ul/li/text()'))
# child::*当前节点的所有子元素
print(tree.xpath('//div[@id="testid"]/child::*'))
# 定位某节点下为ol的子节点下的所有节点内容
print(tree.xpath('//div[@id="testid"]/child::ol/child::*/text()'))

""" attribute：选取当前节点的所有属性 """
# attribute定位id属性值
print(tree.xpath('//div/attribute::id'))
# 定位当前节点的所有属性
print(tree.xpath('//div[@id="testid"]/attribute::*'))

""" ancestor：父辈元素 / ancestor-or-self：父辈元素及当前元素 """
# 定位父辈div元素的price属性
print(tree.xpath('//div[@id="testid"]/ancestor::div/@price'))
# 所有父辈div元素
print(tree.xpath('//div[@id="testid"]/ancestor::div'))
# 所有父辈及当前节点div元素
print(tree.xpath('//div[@id="testid"]/ancestor-or-self::div'))

""" following :选取文档中当前节点的结束标签【之后】的所有节点 """
# 定位testid之后不包含id属性的div标签下所有的li中第一个li的text属性
print(tree.xpath('//div[@id="testid"]/following::div[not(@id)]//li[1]/text()'))

""" preceding：选取文档中当前节点的开始标签【之前】的所有节点 """
# 记住是标签开始之前，同级前节点及其子节点
print(tree.xpath('//div[@id="testid"]/preceding::div/ul/li[1]/text()'))

""" parent：选取当前节点的父节点 """
print(tree.xpath('//li[@data="one"]/parent::ol/li[last()]/text()'))

""" count：统计 """
# 节点统计
print(tree.xpath('count(//li[@data])'))

""" concat：字符串连接 """
print(tree.xpath('concat(//li[@data="one"]/text(),//li[@data="three"]/text())'))
print(tree.xpath('concat(//li[@code="84"]/text(),//li[@code="223"]/text())'))

""" contains(string1,string2)：如果 string1 包含 string2，则返回 true，否则返回 false """
print(tree.xpath('//h3[contains(text(),"这里")]/a/text()'))
print(tree.xpath('//div[@id="go"]//li[contains(@class,"it1")]/text()'))

""" not：布尔值（否） """
print(tree.xpath('count(//li[not(@data)])'))