import json

data1 = {"name": "jingluo", "age": 18}

print(type(str(data1)))  # 不是json类型

data2 = json.dumps(data1)
print(type(data2))
data3 = json.dumps(2)
print(type(data3))
data = {"a": "A", "c": "C", "b": "B", "name": "鲸落"}
print("排序", json.dumps(data, sort_keys=True))
print("缩进", json.dumps(data, indent=4))
print("紧凑", json.dumps(data, separators=(",", ":")))

data[(1, 2)] = "元祖"
print(data)
print(json.dumps(data, skipkeys=True, ensure_ascii=False))  # skipkeys=True跳过异常过滤 ensure_ascii=False 解决编码问题

with open("test.json","w",encoding="utf-8")as f:
    # f.write(str(data)) # 不是json格式
    # f.write(json.dumps(data, skipkeys=True, ensure_ascii=False))
    json.dump(data,f,skipkeys=True, ensure_ascii=False)