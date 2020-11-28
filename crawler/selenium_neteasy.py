#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_neteasy.py
#   Last Modified : 2020-11-24 14:48
#   Describe      : 
#
# ====================================================

import sys
# import os

from selenium import webdriver

url = 'https://www.163.com'
driver = webdriver.Chrome(keep_alive=True)
driver.get(url)
login_btn = driver.find_element_by_xpath('//*[@id="js_N_nav_login_title"]')
login_btn.click()
driver.switch_to_frame('x-URS-iframe1606198516015.6833')

email_input = driver.find_element_by_xpath('//*[@id="auto-id-1606198517855"]')
email_input.send_keys('cxysailor@163.com')
#  print(email_input)
