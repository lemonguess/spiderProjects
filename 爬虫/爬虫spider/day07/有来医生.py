from requests_html import HTMLSession
import csv


class Spider:
    def __init__(self):
        self.session = HTMLSession()
        self.level1_url = "https://www.youlai.cn/dise/pk_1_0_1.html"  # 一级分类
        self.HomeUrl = "https://www.youlai.cn"  # 主页 我们要拼接的

    def parseLevel1(self):
        # 解析一级中所有的病症分类
        response = self.session.get(url=self.level1_url)
        level1List = response.html.xpath('//dl[@class="textList"]//a/@href')  # 拿到a连接
        level1Title = response.html.xpath('//dl[@class="textList"]//a/text()')  # 拿到内容
        # for循环一个一个传 传给下面的相关文章的解析函数
        for index in range(0, len(level1List)):
            self.parseArticleHome(level1List[index], level1Title[index])  # 通过下标取值
            # break

    def parseArticleHome(self, url, title):
        """
            相关文章的解析函数
        :return:
        """
        articleHomeUrl = (self.HomeUrl + url).replace('dise/', 'dise/articlelist/').replace('.html', '_%s.html')
        page = 1
        isPage = True
        endPage = 1
        while isPage:
            if page > endPage:  # 超过最大页数
                break
            response = self.session.get(url=articleHomeUrl % page)
            if endPage == 1:
                endPage = int(response.html.xpath('//div[@class="pageyl"]//li[last()-1]/a/text()')[0])
                # print(type(endPage))
            articleList = self.getArticleList(response)
            self.parseArticle(articleList)
            page += 1
            # break

    def getArticleList(self, response):
        """
            获取文章的url列表
        :return:
        """
        return response.html.xpath('//ul[@class="article_left article_l_list bd_none"]//h3/a/@href')

    def parseArticle(self, articleList):
        """
         解析文章详细信息
        :param articleList:
        :return:
        """
        for url in articleList:
            response = self.session.get(url=self.HomeUrl + url)  # 拼接链接
            title = response.html.xpath('//h3[@class="v_title"]/text()')[0]
            createTime = response.html.xpath('//span[@class="fl_left time"]/text()')[0]
            readNum = response.html.xpath('//span[@class="fl_left num"]/text()')[0].replace("阅读：", "")
            doctor = response.html.xpath('//dl[@class="doc_pic_box pdTop10 clearfix"]/dd//li/strong/text()')[0]
            hospital = response.html.xpath('//dl[@class="doc_pic_box pdTop10 clearfix"]/dd//p[1]/text()')[0]
            section = response.html.xpath('//dl[@class="doc_pic_box pdTop10 clearfix"]/dd//p[2]/text()')[0]
            text = response.html.xpath('//div[@class="text"]//text()')
            text1 = ''.join(text).strip()
            with open("内科文章.csv", "a+", encoding="utf-8", newline="")as f:
                writer = csv.writer(f)
                writer.writerow((title, createTime, readNum, doctor, hospital, section, text1))
            print(title, createTime, readNum, doctor, hospital, section, text1)

    def run(self):
        self.parseLevel1()


if __name__ == '__main__':
    spider = Spider()
    headers = ('文章标题', '发表时间', '阅读数', '医生', "医院", "科室", "文章")
    with open("内科文章.csv", "a+", encoding="utf-8", newline="")as f:
        writer = csv.writer(f)
        writer.writerow(headers)
    spider.run()
"""
    /dise/1.html
    https://www.youlai.cn/dise/1.html
    https://www.youlai.cn/dise/articlelist/1_1.html
    /yyk/article/355773.html
    https://www.youlai.cn/yyk/article/355773.html
"""
