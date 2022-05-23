"""
    1. 请求页面
    2. 得到详细链接
    3. 请求详细链接
    4. 拿出图片链接
    5. 下载

    1. 请求页面
    2. 拿出图片ID
    3. 拼接下载链接
    4. 下载
"""
from requests_html import HTMLSession

session = HTMLSession()
url = "https://wallhaven.cc/latest?page="

# imgList=[]
# for page in range(1,2):
#     response = session.get(url=url+str(page))
#     imgUrl = response.html.xpath('//a[@class="preview"]/@href')
#     for url in imgUrl:
#         imgList.append(url)
# print(imgList)

imgList = ['https://wallhaven.cc/w/o317km', 'https://wallhaven.cc/w/721xdv', 'https://wallhaven.cc/w/g7q13l',
           'https://wallhaven.cc/w/j31l6q', 'https://wallhaven.cc/w/l3wger', 'https://wallhaven.cc/w/y8ekzk',
           'https://wallhaven.cc/w/6o5e96', 'https://wallhaven.cc/w/28d6p9', 'https://wallhaven.cc/w/wq63p6',
           'https://wallhaven.cc/w/dpkv93', 'https://wallhaven.cc/w/rdyevq', 'https://wallhaven.cc/w/9m2k3d',
           'https://wallhaven.cc/w/721xyv', 'https://wallhaven.cc/w/pkwmqe', 'https://wallhaven.cc/w/6o5ev6',
           'https://wallhaven.cc/w/m91oxk', 'https://wallhaven.cc/w/9m2kjd', 'https://wallhaven.cc/w/k71jp7',
           'https://wallhaven.cc/w/rdyekq', 'https://wallhaven.cc/w/1kdo93', 'https://wallhaven.cc/w/q23p1d',
           'https://wallhaven.cc/w/z8qvlg', 'https://wallhaven.cc/w/6o5ex6', 'https://wallhaven.cc/w/j31l2q']
for img in imgList:
    id = img[-6:]
    img_img = 'jpg'
    url = f"https://w.wallhaven.cc/full/{id[:2]}/wallhaven-{id}.{img_img}"
    response = session.get(url=url)
    if response.status_code != 200:
        img_img = "png"
        url = f"https://w.wallhaven.cc/full/{id[:2]}/wallhaven-{id}.{img_img}"
        response = session.get(url=url)
    with open(f"image/{id}.{img_img}","wb")as f:
        f.write(response.content)
        print(f"{id}下载完成")
"""
    https://wallhaven.cc/w/28d6p9 a链接
    https://w.wallhaven.cc/full/28/wallhaven-28d6p9.jpg

    https://wallhaven.cc/w/wq63p6
    https://w.wallhaven.cc/full/wq/wallhaven-wq63p6.jpg
"""
