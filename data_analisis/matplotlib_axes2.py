#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_axes2.py
#   Last Modified : 2020-12-08 21:21
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class SettingAxes(object):
    """docstring for SettingAxes"""
    def __init__(self):
        super(SettingAxes, self).__init__()
        self.x = np.linspace(-3, 3, 50)
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        plt.figure()
        plt.plot(self.x, self.y1)
        plt.plot(self.x, self.y2, color='green', linewidth=1.0, linestyle='--')

        # 设置数据区间
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        # 设置坐标轴标签
        plt.xlabel('I am x')
        plt.ylabel('I am y')

        # 设置坐标轴刻度
        plt.xticks(self.new_ticks)
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

        # 获取坐标轴 gca - get current axis
        ax = plt.gca()
        # 设置图片边框线颜色
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # 设置坐标原点
        ax.xaxis.set_ticks_position('bottom')  # x轴刻度在底部
        ax.yaxis.set_ticks_position('left')  # y轴刻度在左侧
        # 设置坐标原点到(0,0)点处
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))

        plt.show()


if __name__ == "__main__":
    sa = SettingAxes()
    sa.generate_figure()
