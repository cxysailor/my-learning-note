#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_city.py
#   Last Modified : 2021-01-09 11:12
#   Describe      : 
#
# ====================================================
import requests
from lxml import etree


class GetAllCity():
    """获取真气网上的城市名称"""
    def __init__(self):
        super(GetAllCity, self).__init__()
        self.url = 'https://www.aqistudy.cn/historydata/'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.city_list = []  # 存储城市

    def get_info(self):
        """获取信息"""
        page_text = requests.get(url=self.url, headers=self.headers).text
        #  print(page_text)
        tree = etree.HTML(page_text)
        # 将两个xpath表达式写在一起 - 这个例子的知识点
        a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
        for a in a_list:
            city = a.xpath('./text()')[0]
            self.city_list.append(city)
        print(self.city_list, len(self.city_list))


if __name__ == "__main__":
    gac = GetAllCity()
    gac.get_info()
