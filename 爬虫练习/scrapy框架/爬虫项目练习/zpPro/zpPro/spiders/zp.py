import scrapy


class ZpSpider(scrapy.Spider):
    name = 'zp'
    allowed_domains = ['ww.xx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&city=101190100&industry=&position=']

    def start_requests(self):
        cookies = 'acw_tc=0bdd34b616268942927937274e01dcb344df0008af9daee6949798439e3da1; __zp_stoken__=56b9cfGMncBEediJJY3lvMWQhGTZgChICCm5vW3klBF9we2ZuID97LAQ9L3BCSW1%2BLX9lHQd7E0sdf1A2bkNwBGQJRWtTCFUpZWUNXk0LOz1AUCtWQ3chShJUJ1ETFE0DHVx1IA57bDQYNmwW'
        '''
        将cookie转成字典类型
        '''
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,cookies=cookies)

    def parse(self, response):
        print(response.text)
        print(type(response))
