from Cryptodome.Cipher import DES
import binascii
from time import time
import random
class MyDESCipher:
    def __init__(self,key,iv):
        self.key = key
        self.iv = iv

    def encryption(self,data):
        '''

        :param data:
        :return:
        '''
        cipher = DES.new(self.key,DES.MODE_CFB,self.iv)
        data = data.encode()
        return binascii.b2a_hex(cipher.encrypt(data))

    def decryption(self,data):
        '''
        解密
        :param data:十六进制转二进制
        :return:
        '''
        data = binascii.a2b_hex(data)
        cipher =DES.new(self.key,DES.MODE_CFB,self.iv)#创建相同的规则
        return cipher.decrypt(data).decode()



if __name__ == '__main__':
    #需要加密的数据
    word = 'hello world'
    lts = str(int(time() * 1000))  # 获取当前时间戳
    salt = lts + str(random.randint(0, 9))  # 获取salt
    sign = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"  # 获取sign

    # 秘钥
    key = b'maquYIGE'
    iv = b'12345678'

    myDEFCipher = MyDESCipher(key,iv)
    res = myDEFCipher.encryption(sign)
    print(res)

    data = myDEFCipher.decryption(res)
    print(data)
