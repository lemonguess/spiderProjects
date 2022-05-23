import scrapy
import logging
import re
logger = logging.getLogger(__name__)


class LoginSpider(scrapy.Spider):
    name = 'login'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://user.qzone.qq.com/137790410']

    def start_requests(self):
        cookies = '_qpsvr_localtk=0.032031576065538525; pgv_pvid=7398176695; pgv_info=ssid=s6845151766; ptui_loginuin=137790410; pt_sms_phone=182******12; uin=o0137790410; skey=@hxIqnEx2g; RK=zHoIClwbT6; ptcz=f49d5f29fb37aa63c118f9a483cf7203ad8a307d90956caf7e211bfc1816d176; p_uin=o0137790410; pt4_token=2gN*NeXTvEP95N5yBHe34aMt*LswUBAalCuyVhPB9js_; p_skey=oF5OEfbVQfLT0PUj62takgMalejK3CvNLA7ogdFv8ks_; qz_screen=1536x864; qzmusicplayer=qzone_player_137790410_1626889844511; qqmusic_uin=0137790410; qqmusic_key=@hxIqnEx2g; qqmusic_fromtag=6; 137790410_todaycount=0; 137790410_totalcount=26180; QZ_FE_WEBP_SUPPORT=1'
        '''
        将cookie转成字典类型
        '''
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
        #手动发送request
        yield scrapy.Request(url=self.start_urls[0],
                             dont_filter=True,
                             callback=self.parse,
                             cookies=cookies)#dont_filter:是否过滤(调度器会默认过滤重复的url，可不写)

    # def start_requests(self):
    #     #手动发送post请求
    #     yield scrapy.FormRequest(url=self.start_urls,formdata={ '':'','':''},callback=self.parse)
    def parse(self,response):
        print('a')
        with open('./qzone.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        #print(response.text)
        #logger.warning(re.findall('罗林',response.text))
