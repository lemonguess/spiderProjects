from PIL import Image
new_img = Image.new('RBG',(312,116))
#创建图片
#img = Image.new('RGB',(300,300),(255,0,0))
#保存图片
#img.save('red.png')

#读取图片
#img = Image.open('red.png')
#img.show()#显示图片

#裁剪图片
# rangle = (2000,200,3000,2000)
# i = Image.open('text.jpg')#打开本地的图片
# frame = i.crop(rangle)
#frame.show()

#拼接图片
# green = Image.new('RGB',(400,400),(0,255,0))
# green.paste(frame,(0,0))
# green.show()

#转换模式.RGB.L(灰度模式——去掉颜色)
# img = Image.open('text.jpg')
# img_l = img.convert('L')
# img_l.show()

#分割通道 R,G,B
# img = Image.open('text.jpg')
# R,G,B = img.split()
# print(R,'\n',G,'\n',B)

#补充
# img = Image.open('red.png')
# print(list(img.getdata()))  #获取全部像素点的颜色值
# print(img.getpixel((10,10)))#获取指定像素点的颜色值
