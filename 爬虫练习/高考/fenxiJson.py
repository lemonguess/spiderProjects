import json
for i in range(1,144):
    with open(f'./urls/school_{i}.json','r',encoding='utf-8') as fp:
        s = json.load(fp)
    object_list = s['data']['item']
    for object in object_list:
        school_name=object['name']
        school_id=object['school_id']
        school_url = f"https://gkcx.eol.cn/school/{school_id}/provinceline"
        print(school_name,school_url)


