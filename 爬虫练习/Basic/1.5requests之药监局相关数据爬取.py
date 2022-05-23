import requests
import json
#获取不同企业的ID值
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
list_id=[]#存储所有ID
for i in range(0,2):
    param = {
        'on':'true',
        'page':i,
        'pageSize':'15',
        'productName':'',
        'conditionType':'1',
        'applyname':'',
        'applysn':'',
    }
    json_ids = requests.post(url=url,params=param,headers=headers).json()
    for dic in json_ids['list']:
        list_id.append(dic['ID'])

#获取企业详情
post_url ='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
all_data_list = []#存储所有企业详情信息
for id1 in list_id:
    data ={
        'id': id1
    }
    detail_json = requests.post(url=post_url,params=data,headers=headers).json()
    all_data_list.append(detail_json)



fp = open('./化妆品公司详情.json','w',encoding='utf-8')
json.dump(all_data_list,fp=fp,ensure_ascii=False)