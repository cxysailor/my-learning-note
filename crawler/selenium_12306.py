#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_12306.py
#   Last Modified : 2020-12-16 17:48
#   Describe      :
#
# ====================================================
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image
from chaojiying_Python.chaojiying import Chaojiying_Client

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()  # 最大化窗口
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    # 获取帐号登录按钮并点击，进入到帐号密码登录
    login_by_user = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[2]/a')
    login_by_user.click()
    time.sleep(1)
    # 截取整个页面并保存
    driver.save_screenshot('./images/hlg.png')
    # 获取验证码区域的标签
    code_tag = driver.find_element(By.ID, 'J-loginImg')
    # 获取它的坐标及尺寸
    x, y = code_tag.location['x'], code_tag.location['y']
    w, h = code_tag.size['width'], code_tag.size['height']
    #  print(x, y, w, h)
    # 计算右下角的坐标
    x1 = x + w
    y1 = y + h
    # 将2个坐标做一个元组，确定要截取的区域
    rangle = (x, y, x1, y1)

    # 实例化Image并打开截取下来的整个页面图片
    img = Image.open('./images/hlg.png')
    # 截取确定好的区域
    code_img = img.crop(rangle)
    # 保存截取的验证码
    code_img.save('./images/code.png')

    # 使用超级鹰识别验证码
    chaojiying = Chaojiying_Client('user', 'password', 'id')
    im = open('./images/code.png', 'rb').read()
    #  print(chaojiying.PostPic(im, 9004))
    result = chaojiying.PostPic(im, 9004)['pic_str']  # 获取返回的坐标值 - 是一个字符串
    #  print(result)
    #  print(type(result))

    # 对返回值进行处理
    if '|' in result:
        cos = list(result.split('|'))  # 将每组坐标放入一个列表cos
    else:
        cos = list(result.split(','))  # 没有|分隔，即只有一组坐标放入列表cos

    # 遍历列表cos并取出其中的每一组坐标，获取其中的横坐标与纵坐标(需要转换为int类型)
    # 接着使用动作链完成点击
    for co in enumerate(cos):
        x = int(co[1].split(',')[0])  # 横坐标
        y = int(co[1].split(',')[1])  # 纵坐标
        # 使用动作链的move_to_element_with_offset()方法完成点击
        # 坐标x,y是相对于验证码区域的值，所以传入上面获取的验证码code_tag
        ActionChains(driver).move_to_element_with_offset(code_tag, x, y).click().perform()
        time.sleep(1)

    # 获取用户名输入框及密码输入框
    u_input = driver.find_element(By.ID, 'J-userName')
    p_input = driver.find_element(By.ID, 'J-password')
    # 输入用户名及密码
    u_input.send_keys('xxx')
    p_input.send_keys('xxxxxx')

    # 获取登录按钮
    login_btn = driver.find_element(By.ID, 'J-login')
    # 点击登录按钮
    login_btn.click()

    time.sleep(10)
    driver.quit()
