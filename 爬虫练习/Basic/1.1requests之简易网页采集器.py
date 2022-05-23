import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#step1:指定url
url = 'https://www.douban.com/search?'
    #处理url携带的参数：封装到字典中
kw = input('enter a word:')
param={
    'q':kw
}
#step2:发起请求(此处对应的url是携带参数的，并且请求过程中处理了参数)
response = requests.get(url=url,params=param,headers=headers)
#step3:获取响应数据(.text返回的是字符串形式的响应数据)
page_text = response.text
#step4:持久化存储
filename = kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename+'保存成功！')