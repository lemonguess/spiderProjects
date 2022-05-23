#可迭代对象
l1 = [1,3,5,7,"q"]
'''
print(l1.__iter__())
<list_iterator object at 0x00000244AE48C550>
===============================================
python中处理异常
try:
    可能出错的代码
except(异常类型):当只有一种异常类型的时候就可以省略这个异常类型
    如果报错就会执行的代码
else:
    不报错就要执行的代码
finally:
    无论是否报错都要执行的代码
'''

#列表迭代器
iterator = l1.__iter__()
while True:
    try:
        res = iterator.__next__()

    except :
        break
    else:
        print(res)

dict_info = {'name':'lmj','age':'18','gender':'man'}
dic = dict_info.__iter__()
#遍历字典是遍历字典的键
while True:
    try:
        res = dic.__next__()
    except:
        break
    else:
        print(res,dict_info[res])