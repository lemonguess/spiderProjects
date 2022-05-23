import csv
# 这种方式读取到的每一条数据是一个列表，所以需要通过下标的方式获取具体某一个值
# with open("student.csv",'r',encoding="utf-8",newline="")as f:
#     reader = csv.reader(f)
#     for x in reader:
#         print(x)
#         print(x[0])

with open("student.csv",'r',encoding="utf-8",newline="")as f:
    reader = csv.DictReader(f)
    for x in reader:
        print(x)
        print(x["name"])
        print(x.get("name"))
