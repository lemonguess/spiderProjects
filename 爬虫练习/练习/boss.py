from requests_html import HTMLSession
import re
session = HTMLSession()

url = 'https://www.zhipin.com/c101190100/?query=python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&page=1&ka=page-1'
url_first = 'https://www.zhipin.com/?ka=header-home'
cookies = 'sid=sem_pz_sgm_title2; __zp_seo_uuid__=5fd30e48-5e1c-4821-bcfb-0ba9bc7a7cc9; __g=sem_pz_sgm_title2; __l=r=&l=%2Fwww.zhipin.com%2Fnanjing%2F%3Fsid%3Dsem_pz_sgm_title2&s=1&g=%2Fwww.zhipin.com%2Fnanjing%2F%3Fsid%3Dsem_pz_sgm_title2&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1626280085; lastCity=100010000; ___gtid=-1231242919; __fid=7e20d8abc628b8c9eeefb26a23281ab1; __c=1626280085; __a=59544295.1626280085..1626280085.17.1.17.17; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1626282758; __zp_stoken__=c508cZwdfcTYpbA42XxgCLUxhbxZQXiNvUncRNHV%2FUlVPemA3Vnc2eXtHEh5zKGldJi4HBmVdNR0lbhxBKiB3KA9QFnV2WhscJQALXhJJc3ZybElpXA8bdxoubVdVRSAEFg0XO2wgThBHUQZh'
cookie= {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
print(cookie)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
Request_headers = {
'authority': 'www.zhipin.com',
'method': 'GET',
'path': '/c101190100/?query=python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&page=1&ka=page-1',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
 'cookie' :cookies,
#'cookie': 'sid=sem_pz_sgm_title2; __zp_seo_uuid__=5fd30e48-5e1c-4821-bcfb-0ba9bc7a7cc9; __g=sem_pz_sgm_title2; __l=r=&l=%2Fwww.zhipin.com%2Fnanjing%2F%3Fsid%3Dsem_pz_sgm_title2&s=1&g=%2Fwww.zhipin.com%2Fnanjing%2F%3Fsid%3Dsem_pz_sgm_title2&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1626280085; lastCity=100010000; __c=1626280085; __a=59544295.1626280085..1626280085.14.1.14.14; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1626281388; __zp_stoken__=c508cZwdfcTYpEVF%2Fc2UVLUxhbxZQWip%2FaB8RNHV%2FUksQJmEhVnc2eXtHEhFQLmkkJi4HBmVdNTtsGDpBQSgOLFUtdQV4OnMfWB9qWHdJc3ZybEkQXAk4eBoubVdVRSAEFg0XO2wgThBHUQZh',
'referer': 'https://www.zhipin.com/c101190100/?query=python%E7%88%AC%E8%99%AB%E5%B7%A5%E7%A8%8B%E5%B8%88&page=2&ka=page-2',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}

# response = session.get(url = url_first,headers=headers)
response = session.get(url = url,headers=Request_headers)
response.encoding = 'utf-8'
n = re.findall(r'爬虫',response.text)
if len(n) == 0 :
    print('==========爬取失败=========',response.text)
else:
    print('==========爬取成功=========',response.text)