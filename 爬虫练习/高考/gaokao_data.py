import json
with open('./urls/school_1.json','r',encoding='utf-8') as fp:
    j=json.load(fp)
    print(j)
    print(type(j),'\n',j)


