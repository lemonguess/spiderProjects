import scrapy


class FirstSpider(scrapy.Spider):
    #�����ļ������ƣ�����Դ�ļ���Ψһ��ʶ
    name = 'first'
    #���������:�����޶�start urls�б�����Щurl���Խ��������ͣ�ͨ�������ã�
    allowed_domains = ['www.xxx.com']
    #��ʼ��url�б����б��д�ŵ�url�ᱻscrapy�Զ�����ķ���
    start_urls = ['http://www.baidu.com/','http://www.sogou.com']

    #���������ݽ�����response������ʾ�ľ�������ɹ����Ӧ����Ӧ����
    def parse(self, response):
        print(response)
