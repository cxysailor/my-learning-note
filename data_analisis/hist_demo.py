#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : hist_demo.py
#   Last Modified : 2020-11-30 10:51
#   Describe      : 
#
# ====================================================

import random
from matplotlib import pyplot as plt
#  from matplotlib import font_manager


class HistDemo(object):
    """直方图"""

    def __init__(self):
        super(HistDemo, self).__init__()
        # 解决中文显示的问题
        plt.rcParams['font.family'] = ['WenQuanYi Micro Hei']
        plt.rcParams['axes.unicode_minus'] = False
        # 数据列表
        self.datas = []
        # 组距
        self.bin_width = 3
        # 设置图形大小
        plt.figure(figsize=(20, 8), dpi=80)

    def generate_numbers(self):
        """生成数据"""
        for _ in range(250):
            data = random.randrange(70, 151)
            self.datas.append(data)

    def show_hist(self):
        """生成直方图"""
        self.generate_numbers()
        # 分组数量 = 极差/组距
        bin_num = int((max(self.datas) - min(self.datas)) / self.bin_width)
        # 画直方图
        plt.hist(self.datas, bin_num)
        # 设置x轴的刻度
        plt.xticks(range(min(self.datas), max(self.datas) + self.bin_width, self.bin_width))
        # 添加x轴标题
        plt.xlabel('电影时长(分钟)')
        # 添加y轴标题
        plt.ylabel('电影的数量')
        # 添加标题
        plt.title('直方图-电影时长分布统计图')
        # 添加网格线
        plt.grid()
        # 显示图形
        plt.show()


if __name__ == "__main__":
    hd = HistDemo()
    hd.show_hist()

