#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : selenium_taobao.py
#   Last Modified : 2020-08-29 00:43
#   Describe      : 
#
# ====================================================
import time
from selenium import webdriver


browser = webdriver.Chrome()


class SeleniumGetTaobao(object):
    """docstring for ClassName"""
    def __init__(self):
        super(SeleniumGetTaobao, self).__init__()
        self.url = 'http://www.taobao.com'

    def get_info(self):
        """获取淘宝的信息"""
        global browser
        #  browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        browser.get(self.url)
        # 定位搜索输入框标签
        search_input = browser.find_element_by_id('q')
        # 与标签的交互
        search_input.send_keys('iphone')  # 向这个标签传递一个iphone，用来搜索
        # 定位到搜索按钮标签
        search_btn = browser.find_element_by_class_name('btn-search')
        #  search_btn = browser.find_element_by_css_selector('.btn-search')
        time.sleep(2)
        # 执行一段js代码实现向下滚动一屏
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        # 点击搜索按钮
        search_btn.click()
        time.sleep(5)

        # 再次请求另外一个url
        browser.get('https://baidu.com')
        # 点击回退按钮
        browser.back()
        time.sleep(2)
        # 点击前进按钮
        browser.forward()
        time.sleep(5)
        #  browser.quit()


if __name__ == "__main__":
    sgt = SeleniumGetTaobao()
    sgt.get_info()
