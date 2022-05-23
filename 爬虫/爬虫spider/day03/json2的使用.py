import json
"""
    总结：
    json.loads() 是将json格式字符串转为python对象
    json.dumps() python对象转json字符串
    json.dump 将python类型转json写入文件
    json.load() 读取文件json格式数据转成python类型
    
"""
dict2 = '{"name": "jingluo", "age": 18}'
print(type(dict2))
data1 = json.loads(dict2)
print(type(data1))

with open("test.json", "r", encoding="utf-8")as f:
    print(type(f.read()))  # str
    f.seek(0)
    print(type(json.load(f)))  # dict
