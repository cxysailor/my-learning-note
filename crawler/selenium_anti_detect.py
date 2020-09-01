#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_anti_detect.py
#   Last Modified : 2020-08-31 22:41
#   Describe      :
#
# ====================================================
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#  from selenium.webdriver import ChromeOptions


# 实例化Options
chrome_options = Options()
# 添加参数 - 实现无可视化界面
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化ChromeOptions - 实现规避检测
#  options = ChromeOptions()
# 添加参数
#  options.add_experimental_option('excludeSwitches', ['enable-automation'])

#  实例化webdriver，并传入参数
driver = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver',
    options=chrome_options,
    #  options=options
)
driver.get('https://www.baidu.com')

print(driver.page_source)
time.sleep(2)
driver.quit()
