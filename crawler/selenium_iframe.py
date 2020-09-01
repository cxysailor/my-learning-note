#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_iframe.py
#   Last Modified : 2020-08-31 17:58
#   Describe      :
#
# ====================================================
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame('iframeResult')
div_tag = driver.find_element_by_id('draggable')

# 动作链
action = ActionChains(driver=driver)
# 点击并按住div_tag
action.click_and_hold(div_tag)
# 使用循环实现连续拖动div_tag
for i in range(5):
    # move_by_offset(xoffset, yoffset)移动标签，以像素为单位
    # perform()立即执行动作链操作
    action.move_by_offset(17, 0).perform()
    time.sleep(0.3)

# 使用完成，释放动作链
action.release()
#  print(div_tag)
driver.quit()
