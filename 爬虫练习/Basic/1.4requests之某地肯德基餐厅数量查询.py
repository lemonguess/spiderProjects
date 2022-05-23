import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
add = input('请输入需要查询的地点：')

def Num():
    global num
    param = {
        'cname': add,
        'pid': '',
        'pageIndex': '1',
        'pageSize': '10',
    }
    response = requests.post(url=url, params=param, headers=headers)
    data = eval(response.text)
    num= data['Table'][0]['rowcount']
while True:
    num=0
    Num()
    if num >= 1:
        print(f'该地肯德基餐厅的数量为：{num}。')
        add = input('请输入需要查询的地点：')
        Num()
        continue
    else:
        add=input('抱歉，未找到相关搜索结果，请重新搜索：')
        Num()
        continue


