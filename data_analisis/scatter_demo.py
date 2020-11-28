#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : scatter_demo.py
#   Last Modified : 2020-11-28 19:29
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')
plt.rcParams['font.family'] = ['WenQuanYi Micro Hei']                                                                   
plt.rcParams['axes.unicode_minus'] = False


class Scatter_Demo():
    """散点图"""
    def __init__(self):
        # 3月份温度
        self.march = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
        # 10月份温度
        self.october = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]
        # 日期
        self.x_march = list(range(1, 32))
        self.x_october = list(range(51, 82))

    def paint_demo(self):
        """画散点图"""
        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)
        # 设置网格线
        plt.grid()
        # 绘制散点图
        plt.scatter(self.x_march, self.march, c='red', label='3月份')
        plt.scatter(self.x_october, self.october, c='green', label='10月份')
        # 调整x轴的刻度
        x = self.x_march + self.x_october
        xtick_labels = [f"3月{i}日" for i in self.x_march]
        xtick_labels += [f"10月{i - 50}日" for i in self.x_october]
        plt.xticks(x[::3], xtick_labels[::3], rotation=45)
        # 添加图例
        plt.legend(loc='upper left', prop=my_font)
        # 添加描述信息
        plt.xlabel('日期', fontproperties=my_font)
        plt.ylabel('温度', fontproperties=my_font)
        plt.title('3月份与10月份温度散点图', fontproperties=my_font)
        # 显示图形
        plt.show()


if __name__ == '__main__':
    sd = Scatter_Demo()
    sd.paint_demo()
