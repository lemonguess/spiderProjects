#json字符串——四种方法
import json
data1={
    'a':'1',
    'b':'2'
}
# data2 = json.dump(data1)
# json.load()

data3 = json.dumps(2)
print(type(data3))

data4 = {
    'a':'A','b':'B','c':'C'
}
print('排序：',json.dumps(data4,sort_keys=False))
print('缩进：',json.dumps(data4,indent=4))
print('紧凑：',json.dumps(data4,separators=(',',':')))

data4[(1,2)]='元组'
print(data4)
print(json.dumps(data4,skipkeys=True,ensure_ascii=False))#跳过异常过滤/解决编码问题

# with open('test.json','w',encoding='utf-8') as fp:
#     fp.write(str(data4))
#     fp.write(json.dumps(data4,skipkeys=True,ensure_ascii=False))
#     json.dump()
