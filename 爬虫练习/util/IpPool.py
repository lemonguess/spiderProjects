import re

from requests_html import HTMLSession

def getIP(dic):
    ip_list = []
    for i in range(0,len(dic["RESULT"])):
        ip_dict=dic["RESULT"][i]
        ip=f'{ip_dict["ip"]}:{ip_dict["port"]}'
        ip_list.append(ip)
    return ip_list





#getip.get('NAME')#获取模块包里的值