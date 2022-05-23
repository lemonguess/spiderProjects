import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions as EC #提供预期判断的方法，指定等待的元素,能够完成使命操作
from selenium.webdriver.common.by import By #定位元素
from selenium.webdriver.common.action_chains import ActionChains#导入动作链
from requests_html import HTMLSession
from io import BytesIO
from PIL import Image
from time import sleep
import re




def get_merge_image(img,img_list):
    '''
    裁剪后拼接图片
    :param img:要处理的素材图
    :param img_list:每个图片的定位信息
    :return:
    '''
    #裁剪
    img_list_upper = []
    img_list_down = []
    for img_info in img_list:
        if img_info['y'] == -58:
            rangle = abs(img_info['x']),abs(img_info['y']),abs(img_info['x'])+10,abs(img_info['y'])+58
            img_list_upper.append(img.crop(rangle))
        elif img_info['y'] == 0:
            rangle = abs(img_info['x']), abs(img_info['y']), abs(img_info['x']) + 10, abs(img_info['y']) + 58
            img_list_down.append(img.crop(rangle))
    #粘贴图片
    new_img = Image.new('RGB',(260,116))#新建画布
    x_offset = 0
    for i in range(0,len(img_list_upper)):
        img_info = img_list[i] #图片的坐标
        new_img.paste(img_list_upper[i],(x_offset,0))
        new_img.paste(img_list_down[i], (x_offset, 58))
        x_offset += 10
    #new_img.show()
    #print('图片拼接完成！')
    return new_img


def get_image(driver, div_class):
    '''
    获取素材图及每个div背景图定位坐标
    :param driver:
    :param div_class:
    :return:
    '''
    # 获取所有图片元素
    background_images = driver.find_elements_by_class_name(div_class)
    #img_url = None
    img_list = []
    img_url = None
    for image in background_images:
        # 拿到每一个图片元素 div
        # print(image.get_attribute('style'))
        img_info = {}

        img = re.findall(r'url\("(.*?)"\); background-position: (.+?)px (.+?)px',
                         image.get_attribute('style')
                         )[0]
        img_url, img_info['x'], img_info['y'] = img
        img_info['x'] = int(img_info['x'])
        img_info['y'] = int(img_info['y'])
        img_list.append(img_info)

        #print(img_list)
    session = HTMLSession()
    response = session.get(img_url).content
    img_data = BytesIO(response)
    img = Image.open(img_data)
    #img.show()

    return get_merge_image(img,img_list)

def is_similar(complete_img,gap_img,x,y):
    '''
    通过对比像素
    :param complete_img:
    :param gap_img:
    :return:
    '''
    #两张图片相同像素点的RGB值
    complete_pixel = complete_img.getpixel((x,y))
    gap_pixel = gap_img.getpixel((x,y))

    for i in range(0,3):
        if abs(complete_pixel[i]-gap_pixel[i]) >= 50 :
            #两个像素点的颜色不一致，返回False
            return False
    else:
        return True

def get_diff_localtion(complete_img,gap_img):
    '''
    找到缺口位置
    :param complete_img:完整图
    :param gap_img:缺口图
    :return:
    '''
    for x in range(1,259):
        for y in range(1,115):
            if not is_similar(complete_img,gap_img,x,y):
                #两个像素点的颜色不一致
                print('小黑块位置：x',x)
                return x

def get_track(x):
    #初速度
    v= 0
    #单位时间，统计轨迹，多时间内的位置
    t=3
    #轨迹列表
    tracks=[]
    #当前的位移
    current = 0
    #到达mid的时候减速
    mid = x * 5 / 8
    x += 10
    while current < x :
        if current <mid:
            a = random.randint(0,5) #加速
        else :
            a = -random.randint(0,5) #减速
        v0=v

        s = v0 *t +random.randint(1,3)*a*(t**2)
        #当前位置
        current += s
        #添加到轨迹列表
        tracks.append(round(s))
        #速度公式
        v= v0 + a*t
    #反向滑动大概位置
    for i in range(4):
        tracks.append(-random.randint(1,3))
    print(tracks)
    # tracks=[]
    # a = 0
    # b = 1
    # while b <= x:
    #
    #     a=random.randint(a,b)
    #     step=random.randint(a,b)
    #     b=random.randint(step,b)
    #     tracks.append(b)
    #     b =random.randint(step, b)+2
    print(tracks)

    return tracks






def main(driver,gt_slider_knob):

    complete_img = get_image(driver,'gt_cut_fullbg_slice')  #完整图
    gap_img = get_image(driver,'gt_cut_bg_slice')      #缺口图

    x = get_diff_localtion(complete_img,gap_img)
    #print(x)
    track = get_track(x)
    ActionChains(driver).click_and_hold(gt_slider_knob).perform()#按住滑块元素
    # for x in track:
    #     ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()#拖动
    #     time=random.randint(0,0.05)
    #     sleep(1)
    s=0
    while s <= x :
        d=random.randint(1,5)
        ActionChains(driver).move_by_offset(xoffset=d,yoffset=0).perform()
        time = random.randint(0, 1)
        sleep(time)
        s=s+d

    ActionChains(driver).release(gt_slider_knob).perform()#释放
    #抓取素材图



    sleep(5)

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')
    driver.maximize_window()  # 设置浏览器界面最大化
    driver.get('http://www.cnbaowen.net/api/geetest/')
    sleep(3)
    # 等待滑块加载完成，再开始获取图片
    wait = WebDriverWait(driver, 20)
    gt_slider_knob = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gt_slider_knob')))  # 滑块

    while True:
        main(driver,gt_slider_knob)
        success = re.findall(r'<div class="gt_ajax_tip gt_success"></div>',driver.page_source)
        if success:
            print('识别成功！')
            break
        else:
            print('识别错误，重试中')
    driver.quit()
