from requests_html import HTMLSession
import requests
import re
from lxml import etree
def getToken():
    '''
    获取cookies
    :return: cookies
    '''
    import json
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    url = 'https://www.zhipin.com/job_detail/7852309438e72a301nF72dm4F1ZU.html?ka=index_rcmd_job_5'
    print('正在获取cookie...')
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                                chrome_options=chrome_options)
    bro.get(url)
    cookie = bro.get_cookies()
    string = str(cookie)
    if len(re.findall('__zp_stoken__', string))==0:
        bro.close()
        print('本次刷新无__zp__stoken__,准备重新载入...')
        return getToken()
    else:
        zp_stoken = re.findall(r"'__zp_stoken__', 'path': '/', 'secure': False, 'value': '(.*?)'}",string)[0]
        cookies={'__zp_stoken__':zp_stoken}
    print(cookies)
    return cookies
    # with open('爬虫项目练习/bossPro/bossPro/cookies.json', 'a+', encoding='utf-8') as f:
    #     f.write(cookies+',')
    # str = ''
    # with open('cookies.json', 'r', encoding='utf-8') as f:
    #     listCookies = json.loads(f.read())
    # print(jsonCookies)
    #cookiestr = '; '.join(item for item in cookie)
    #print(cookiestr)
    # token=re.findall('__zp_stoken__=(.*?);',cookiestr)[0]
    # print('cookie获取成功..\n',token)
    # return f'__zp_stoken__={token}'
def getTokens(times):
    for time in range(times):
        getToken()

def job_page(page,job):
    cookies = '__zp_stoken__=56b9cfGMncBEedmRCC1ogMWQhGTYSb31Gc3tvW3klBEZbaB0QLj97LAQ9fQ4AL3t%2BLX9lHQd7F0ESdDc2Fi91c0J8fQ9Zez9Yd3xlK1ALOz1AUCtWVRFjNEBUJ1ETFEMDHVx1IA57bDQYNmwW'
    print(cookies)
    UA = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'Host': 'www.zhipin.com',
        'Cookie':cookies}
    proxy = {
        'http': '59.58.252.97:30132'
    }
    for i in range(1,page+1):
        url = f'https://www.zhipin.com/c101190100/?query={job}&page={page}&ka=page-{page}'
        res = requests.get(url=url,headers=UA,proxies=proxy)
        page_text = res.text
        print(page_text)
        print(res.status_code)
        # tree=etree.HTML(res)
        # for li in range(1,31):
        #     job_name = tree.xpath(f'//*[@id="main"]/div/div[3]/ul/li[{li}]/div/div[1]/div[1]/div/div[1]/span[1]/a/text()')
        #     place = tree.xpath(f'//*[@id="main"]/div/div[3]/ul/li{li}/div/div[1]/div[1]/div/div[1]/span[2]/span/text()')
        #     print(job_name,place)
    #print(location['hostname'])

if __name__ == '__main__':
    #job = input('请输入要查询的职位名称:')
    job = '医生'
    job_page(1,job)
    #getTokens(1)
