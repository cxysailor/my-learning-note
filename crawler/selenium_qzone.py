#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_qzone.py
#   Last Modified : 2020-08-31 20:37
#   Describe      : 
#
# ====================================================
import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# 请求QQ空间的页面
browser.get('https://i.qq.com/')
# 切换到id为login_frame的iframe中
browser.switch_to.frame('login_frame')
# 获取帐号密码登录按钮标签，其id为switcher_plogin
btn_plogin = browser.find_element_by_id('switcher_plogin')
# 点击btn_plogin按钮
btn_plogin.click()
time.sleep(1)
# 获取帐号输入框和密码输入框
user_input = browser.find_element_by_id('u')  # 帐号输入框
passwd_input = browser.find_element_by_id('p')  # 密码输入框
# 输入帐号与密码
user_input.send_keys('707778247')
time.sleep(1)
passwd_input.send_keys('74@PrIl27')
time.sleep(1)
# 获取并点击登录按钮
btn_login = browser.find_element_by_id('login_button')
btn_login.click()
time.sleep(10)
