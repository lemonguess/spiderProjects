import re
from requests_html import HTMLSession

"""
    1. re.compile 正则表达式语法
    2. re.search  找一个
    3. re.match 从头找一个 没有返回None
    4. re.findall 找所有 返回列表
    
    .       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
    *       匹配0个或多个的表达式
    +       匹配1个或者多个的表达式
    ?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
    []       表示一组字符。
    "|"      A|B，创建一个正则，将匹配A或B。
    
    \s      匹配任何空白字符
    \d      匹配任何数字
    
    
"""

str1 = '<link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索1" title="百度搜索2" />'

result = re.findall('title="(.*?)"', str1)
print(result)

str2 = """ 
<html>
    <body>
    <p>python1</p>
    <p>python2</p>
    <p>python3</p>
    <p>python4</p>
    <div>
        Line 1
    </div>
    </body>
</html>
"""
result2 = re.findall('<p>(.*?)</p>', str2)
result3 = re.findall('<div>(.*?)</div>', str2, re.S)[0].strip()
print(result2)
print(result3)

session = HTMLSession()
response = session.get(url="https://www.kuaidaili.com/free/inha/")
result4 = re.findall('<td data-title="IP">(.*?)</td>',response.text)
print(result4)