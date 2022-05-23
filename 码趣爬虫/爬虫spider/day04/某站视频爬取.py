from requests_html import HTMLSession
import re
session = HTMLSession()
"""
https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/25/86/4278625/4278625_da3-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1625238449&gen=playurlv2&os=cosbv&oi=2936064087&trid=1ff1df2ccbe44000a28611d98ade1317h&platform=html5&upsig=3bd3616ff6dd3a2ea9e769a59347ef20&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000
"""
url = "https://m.bilibili.com/video/BV1Ws411m7dG?spm_id_from=333.5.b_67616d655f7374616e645f616c6f6e65.33"
headers ={
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
response = session.get(url=url,headers=headers)

# print(response.text)

result = re.findall("readyVideoUrl: '(.*?)'",response.text)
print(result)
viedo_res = session.get(url=result[0])
with open("拳皇.mp4","wb")as f:
    f.write(viedo_res.content)
# rule_re = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
# data_list = re.findall(rule_re, response.text)
# formatList = list(set(data_list))
# for i in formatList:
#     print(i)