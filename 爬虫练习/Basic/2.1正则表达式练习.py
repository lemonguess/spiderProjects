import re
#提取出python
key1 = 'javapythonc++php'
re.findall(r'python',key1)
############################################################
#提取hello world
key2 = '<html><h1>hello world</h1></html>'
print(re.findall('<h1>(.*)</h1>',key2))
############################################################
#提取170
key3 = '小明身高170厘米'
print(re.findall('\d+',key3))
##############################################################
#提取出http:// 和 https://
key4 = 'http://baidu.com and https://boob.com'
print(re.findall('https?://',key4))
#############################################################
#提取出hello 输出<html>hello</HtMl>
key5 = 'lalalala<html>hello</HtMl>lalalalaa'
print(re.findall('<.*>',key5))
##############################################################
#提取出hit.
key6 = 'robot@hit.com'
print(re.findall('h.*?\.',key6))
##############################################################
#匹配sas 和 saas saaaaas
key7 = 'sasodfsaasspppssaaaaassaaas'
print(re.findall('sa{1,2}s|saaaaas',key7))


