#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_headless.py
#   Last Modified : 2020-11-15 19:56
#   Describe      :
#
# ====================================================
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 实例化Options
chrome_options = Options()
# 添加2个参数
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 实例化webdriver并加入参数
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)
# 请求一个网址
driver.get('https://www.baidu.com')
# 打印结果验证是否执行了无头浏览器操作
print(driver.page_source)
time.sleep(2)
# 退出webdriver
driver.quit()
