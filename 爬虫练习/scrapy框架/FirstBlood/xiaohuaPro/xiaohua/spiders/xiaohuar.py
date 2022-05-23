import scrapy


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    #allowed_domains = ['www.xxx.com']
    #第一页页面
    start_urls = ['http://www.521609.com/tuku/mxxz/index.html']
    #通用页面（第二页及以后）
    url = 'http://www.521609.com/tuku/mxxz/index_%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a/p/test()').extract_first()
            print(img_name)
        if self.page_num <= 29:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield  scrapy.Request(url=new_url,callback=self.parse)