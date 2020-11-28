#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : bar_demo.py
#   Last Modified : 2020-11-28 19:07
#   Describe      : 
#
# ====================================================
from selenium import webdriver
from matplotlib import pyplot as plt
from matplotlib import font_manager
from matplotlib import rcParams


class BarDemo():
    """docstring for BarDemo"""
    def __init__(self):
        super(BarDemo, self).__init__()
        self.url = 'http://58921.com/alltime/2020'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

        plt.rcParams['font.family'] = ['WenQuanYi Micro Hei']
        plt.rcParams['axes.unicode_minus'] = False
        self.my_font = font_manager.FontProperties(fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')
        self.titles = ['变身特工', '美丽人生', '紫罗兰永恒花园 外传：\n永远与自动手记人偶', '鲨海逃生', '熊出没·\n狂野大陆', '为家而战', '灭绝', '理查德·\n朱维尔的哀歌', '致敬英雄', '士兵顺溜：\n兵王争锋', '狐踪谍影', '守望人', '野猪', '那人那事', '红色圩场', '蕃薯浇米', '武圣关公', '紫罗兰永恒花园外传：\n永远与自动手记人偶', '无影之镜', '中华熊猫'] 
        self.box_office = [10000.02, 5934.65, 4806.61, 4674.65, 3572.58, 1697.85, 1579.98, 565.61, 308.51, 185.94, 109.02, 107.17, 92.72, 54.18, 24.81, 21.14, 20.34, 18.56, 11.10, 9.13]
#  driver = webdriver.Chrome()
#  driver.get(url)
#  tr_tags = driver.find_elements_by_xpath('//*[@id="content"]/div[3]/table/tbody/tr')
#  for tr_list in tr_tags:
#      a_tags = tr_list.find_elements_by_xpath('./td[3]/a')
#      #  print(a_tags)
#      for a_tag in a_tags:
#          title = a_tag.get_attribute('text')
    #  titles.append(title)
#  print(titles)

    def show_bar(self):
        # 设置图形尺寸
        plt.figure(figsize=(20, 8), dpi=80)
        # 绘制条形图
        plt.bar(range(len(self.titles)), self.box_office, width=0.3)
        # 设置标签到x轴
        plt.xticks(range(len(self.titles)), self.titles, fontproperties=self.my_font, rotation=45)
        plt.xlabel('电影名称', fontproperties=self.my_font)
        plt.ylabel('票房(单位:万元)', fontproperties=self.my_font)
        plt.title('2020年电影票房', fontproperties=self.my_font)
        plt.show()


if __name__ == "__main__":
    bd = BarDemo()
    bd.show_bar()
