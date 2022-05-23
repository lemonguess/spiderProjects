'''
1.模拟登录，填写一个错误的账号和密码——发起登录请求
2.抓包看，发现是参数加密
3.查找分析对称加密的方式：{
    1）.AES
    2）.DES——CryptoJS.DES.encrypt()——三个参数
}
4.查找秘钥，应该是8或8的倍数长度的字节
  查找秘钥：b'zxcvbn78'
  分析模式：CFB（可以理解为不同加密规则） (Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
            and ``MODE_OPENPGP`` modes).
  初始化向量值（个字节）
5.加密的数据：qwe123,
'''
from time import time
import random
from Cryptodome.Cipher import DES
import binascii
#秘钥
key = b'maquYIGE'
iv = b'12345678'

#创建一个密码对象,传入秘钥、模式、初始化向量值，可以理解成一个加密规则
cipher = DES.new(key,DES.MODE_CFB,iv=iv)

#需要加密的数据

word = 'hello world'
lts = str(int(time() * 1000))# 获取当前时间戳
salt = lts + str(random.randint(0, 9))# 获取salt
sign = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"# 获取sign
data =sign
print(type(sign.encode()),sign.encode())

res = cipher.encrypt(sign.encode()) #字节数据
res_16= binascii.b2a_hex(res)  #二进制转16进制
print(type(res),res)
print(type(res_16),res_16)




