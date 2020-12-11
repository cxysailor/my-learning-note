#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_bar.py
#   Last Modified : 2020-12-09 19:02
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class MatplotlibBar(object):
    """柱状图"""
    def __init__(self):
        super(MatplotlibBar, self).__init__()
        self.n = 12
        self.X = np.arange(self.n)
        self.Y1 = (1 - self.X / float(self.n)) * np.random.uniform(0.5, 1.0, self.n)
        self.Y2 = (1 - self.X / float(self.n)) * np.random.uniform(0.5, 1.0, self.n)

    def generate_figure(self):
        plt.xlim(-.5, self.n)
        plt.ylim(-1.25, 1.25)

        plt.xticks(())
        plt.yticks(())

        # 绘制柱状图
        plt.bar(self.X, +self.Y1, facecolor='#9999ff', edgecolor='white')
        plt.bar(self.X, -self.Y2, facecolor='#ff9999', edgecolor='white')

        # 在柱状图的顶/底部添加对应数字标签
        # ha - horizotal alignment; va - vertical alignment
        for x, y in zip(self.X, self.Y1):
            plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
        for x, y in zip(self.X, self.Y2):
            plt.text(x, -(y), '%.2f' % y, ha='center', va='top')

        plt.show()


if __name__ == "__main__":
    mb = MatplotlibBar()
    mb.generate_figure()
