import requests
import re
import os
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

#创建一个文件夹，保存所有图片
if not os.path.exists('./qiutuLibs'):
    os.mkdir('./qiutuLibs')

#设置一个通用的url模板
for page_num in range(1,36):
    url = f'https://www.qiushibaike.com/imgrank/page/{page_num}/'
    page_text = requests.get(url=url,headers=headers).text

    img_src_list = re.findall('<div class="thumb">.*?<img src="/(.*?)" alt.*?</div>',page_text,re.S)

    for src in img_src_list:
        #拼接出一个完整的图片url
        src = 'https:/'+src
        #请求到了二进制响应数据
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称,按斜杠切分，取最后一部分
        img_name = src.split('/')[-1]
        imgPath = './qiutuLibs/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！')


