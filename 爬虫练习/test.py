import requests

url = f'https://movie.douban.com/top250?start=25&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    #'Cookie': 'bid=GmDxqnE7fj8; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1206974214.1626986563.1626986563.1626986563.1; __utmb=30149280.0.10.1626986563; __utmc=30149280; __utmz=30149280.1626986563.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1486525743.1626986563.1626986563.1626986563.1; __utmb=223695111.0.10.1626986563; __utmc=223695111; __utmz=223695111.1626986563.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; __gads=ID=e6ac40b7aa0135e1-2231fa767cca006a:T=1626986589:RT=1626986589:S=ALNI_MYqfP0NBFy7jyG5vfV_PJwm6UWHRw; _pk_id.100001.4cf6=394e3fe4e78846fe.1626986562.1.1626987743.1626986562.'
}
response = requests.get(url='https://www.baidu.com/', headers=headers).text
print(response)