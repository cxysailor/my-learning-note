#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_demo.py
#   Last Modified : 2020-08-27 20:29
#   Describe      :
#
# ====================================================
import time
from selenium import webdriver
from lxml import etree

# 实例化驱动器driver
#  global driver
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# 使用driver发起一个get请求
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
# 使用page_source属性获取当前页面的源码数据
page_text = driver.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
#  print(page_text)
time.sleep(5)
#  driver.quit()
