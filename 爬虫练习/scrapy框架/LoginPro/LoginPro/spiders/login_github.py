import scrapy

'''
三要素：1.接口地址：
      2.请求参数：
      3.
commit: Sign in
authenticity_token: CZ4phaN4OjwtZknRs90/HBZirxJtEMWjYGlQkWWQ0o3wThN558sGFKGdZfcoenm5o51RZkiUXnh8SEIAwG3lVg==
login: lemonguess
password: lxc1335
trusted_device: 
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: /login/oauth/authorize?client_id=Iv1.00d5b33fffc873a2&redirect_uri=https%3A%2F%2Flab.github.com%2Flogin%2Fgithub%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM3MmEzMDk0LTcyZGEtNGZmZC05ODNlLTM2M2JlNWNlZDQwMyIsImlhdCI6MTYyNTQ0OTcxOCwiZXhwIjoxNjI1NDUzMzE4fQ.B4yQy0e__XkbB2U76Cn64c3OzSbsGe3k1D635wte_Gk
allow_signup: 
client_id: Iv1.00d5b33fffc873a2
integration: 
required_field_66b6: 
timestamp: 1625449720541
timestamp_secret: 583501a571a26e98ea787adc1b557eb8ff11aad1147f06ca332d89f0860e6b91
-————————————————————————————————————————————————————————————————————————————————————————————————————————————————
commit: Sign in
authenticity_token: fJjeqTGprT5ZwsRXSvWHXwg+lZOlHM+p6TGsW+udqiZFK0ab1VURaCIkuFUsF3lyfxcg6cw2lENlfB6Wk56rRQ==
login: lemonguess
password: lxc13ewr
trusted_device: 
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: /login/oauth/authorize?client_id=Iv1.00d5b33fffc873a2&redirect_uri=https%3A%2F%2Flab.github.com%2Flogin%2Fgithub%2Fcb&state=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM3MmEzMDk0LTcyZGEtNGZmZC05ODNlLTM2M2JlNWNlZDQwMyIsImlhdCI6MTYyNTQ0OTcxOCwiZXhwIjoxNjI1NDUzMzE4fQ.B4yQy0e__XkbB2U76Cn64c3OzSbsGe3k1D635wte_Gk
allow_signup: 
client_id: Iv1.00d5b33fffc873a2
integration: 
required_field_ca2c: 
timestamp: 1625449878060
timestamp_secret: 67515097f0b2b0ff8ac14b3077c62de9a6ee7473339dabc787b33755d768d19c


return HTML
观察两段异同，需要注意的字段：
authenticity_token:         #认证秘钥
required_field_ca2c:        #字段**
timestamp:                  #时间戳：判断秘钥时间，校验是否过期
timestamp_secret:           #时间戳秘钥（公钥）


首先找到秘钥，哪个请求获取到的token？全局搜索。
'''


class LoginGithubSpider(scrapy.Spider):
    name = 'login_github'
    allowed_domains = ['github.com/session']
    start_urls = ['http://github.com/session/']

    def parse(self, response):
        pass
