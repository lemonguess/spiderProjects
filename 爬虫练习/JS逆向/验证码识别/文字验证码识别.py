from PIL import Image
import pytesser3
import numpy as np
import matplotlib.pyplot as plt
img = Image.open('yzm.jpg')
# img = Image.open('01.PNG')

img = img.convert('L')  #转成灰度模式

'''
浅色转白色，深颜色转黑色
界限，阀值，产生两个极端值，最大值和最小值——进行二值/极化

方式：
1.得到所有的像素点的颜色值，求平均值，作为阀值；
2.统计分析，哪个颜色值是分界线（更靠谱一点）。
'''
#1.平均值作为阀值
w,h = img.size #获取图片的大小、宽高
# print(w,h)
#放大
# img = img.resize((w*2,h*2),Image.ANTIALIAS)

# total = list(img.getdata())#获取每个像素点
#
# avg = sum(total)//len(total)
# avg = 200
#2.统计分析获取阀值
img_np = np.array(img)  #图片转数组

img_np = img_np.reshape(1,-1)
print(img_np)
step = 10
count={}
for i in range(0,256,step):
    count[str(i)+'-'+str(i+step-1)] = img_np[(img_np >=i) & (img_np<i+step)].shape[0]
print(count)
plt.xlabel('pixel value')
plt.ylabel('count')
plt.bar(range(0,256,10),count.values())
# plt.show()
# print(img_np)

avg = 200


#二值化
pixes = img.load()
for x in range(w):
    for y in range(h):
        if pixes[x,y] < avg:
            pixes[x,y] = 0
        else:
            pixes[x,y] = 255

#降噪
for x in range(w-1):
    for y in range(h-1):
        count = 0#统计周边白色像素个数
        if pixes[x,y-1]>245:     #上
            count +=1
        if pixes[x,y+1]>245:     #下
            count +=1
        if pixes[x-1,y]>245:     #左
            count +=1
        if pixes[x,y-1]>245:     #右
            count +=1
        if pixes[x-1,y-1]>245:   #左上
            count +=1
        if pixes[x-1,y+1]>245:   #左下
            count +=1
        if pixes[x+1,y-1]>245:   #右上
            count +=1
        if pixes[x+1,y+1]>245:   #右下
            count +=1
        if count > 5:
            pixes[x,y] = 255




img.show()

code = pytesser3.image_to_string(img)
print(code)