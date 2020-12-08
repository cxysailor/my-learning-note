#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_axes.py
#   Last Modified : 2020-12-08 10:43
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class AxesSetting(object):
    """设置坐标轴"""
    def __init__(self):
        super(AxesSetting, self).__init__()
        # x轴的数据
        self.x = np.linspace(-3, 3, 50)
        # y轴的数据
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        # 坐标轴的刻度
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        """生成图形"""
        plt.figure()
        plt.plot(self.x, self.y1, color='red', linewidth=1.0, linestyle='--')
        plt.plot(self.x, self.y2)

        # 设置数据区间
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        # 设置坐标轴标签
        plt.xlabel('I am x')
        plt.ylabel('I am y')

        # 设置坐标轴刻度
        plt.xticks(self.new_ticks)
        # 同时对y轴的刻度字体进行了一些修饰 - 支持正则与Latex
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', '$bad$', '$normal$', '$good$', r'$really\ good$'])

        # 显示图形
        plt.show()


if __name__ == "__main__":
    st = AxesSetting()
    st.generate_figure()
