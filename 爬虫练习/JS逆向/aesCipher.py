from Cryptodome import Random
from Cryptodome.Cipher import AES
import binascii
from time import time
import random
class MyAESCipher:
    def __init__(self,key,iv):
        self.key = key
        self.iv = Random.new().read(AES.block_size)

    def encryption(self,data):
        '''

        :param data:
        :return:
        '''
        cipher = AES.new(self.key,AES.MODE_CFB,self.iv)
        data = data.encode()
        return binascii.b2a_hex(cipher.encrypt(data))

    def decryption(self,data):
        '''
        解密
        :param data:十六进制转二进制
        :return:
        '''
        data = binascii.a2b_hex(data)
        cipher =AES.new(self.key,AES.MODE_CFB,self.iv)#创建相同的规则
        return cipher.decrypt(data).decode()



if __name__ == '__main__':
    #需要加密的数据
    word = 'hello world'
    lts = str(int(time() * 1000))  # 获取当前时间戳
    salt = lts + str(random.randint(0, 9))  # 获取salt
    sign = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"  # 获取sign

    # 秘钥,偏移向量（16位）
    key = b'maquYIGEmaquYIGE'
    #iv = Random.new().read(AES.block_size)

    myAESCipher = MyAESCipher(key,iv)
    res = myAESCipher.encryption(sign)
    print(res)

    data = myAESCipher.decryption(res)
    print(data)
