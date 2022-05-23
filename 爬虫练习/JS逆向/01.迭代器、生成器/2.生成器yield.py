#迭代器的一种

l = [i for i in range(1,11)]
print(l)
l_ = (i for i in range(1,11))
print(l_)



print('='*50)
#生成器函数
def func1():
    for i in range(1,10):
        return i#返回函数的结果并退出函数
    #返回1-10的元素
res = func1()
print(res)


print('='*50)
def func2():
    for i in range(1,10):
        yield i#返回函数的结果
    #返回1-10的元素
res2 = func2()#生成器对象
print(res2)
for i in res2:
    print(i)



print('='*50)
#返回1-100之间的能被3整除的数
def func3():
    for i in range(1,101):
        if i % 3 == 0:
            yield i
res3 = func3()
i_list=[]
for i in res3:
    i_list.append(i)
    print(i)
print(i_list)


print('='*50)
for i in enumerate([i_list]):
    print(i)



print('='*50)
for i in zip([1,55,99,'lmj',5.0],(1,2,3,4)):
    print(i)