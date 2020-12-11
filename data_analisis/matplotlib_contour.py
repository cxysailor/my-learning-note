#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_contour.py
#   Last Modified : 2020-12-09 22:12
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class MatplotlibContour(object):
    """等高线图"""
    def __init__(self):
        super(MatplotlibContour, self).__init__()
        self.n = 256
        self.x = np.linspace(-3, 3, self.n)
        self.y = np.linspace(-3, 3, self.n)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def contour(self, x, y):
        """生成高程的函数"""
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    def generate_figure(self):
        """画等高线"""
        # 填充等高线底色
        # 数字8这里表示的是等高线的疏密程度
        plt.contourf(self.X, self.Y, self.contour(self.X, self.Y), 8, alpha=0.75, cmap=plt.cm.cool)
        # 添加等高线
        C = plt.contour(self.X, self.Y, self.contour(self.X, self.Y), 28, colors='black', linewidths=.5)
        # 在等高线上添加高程数字标签
        plt.clabel(C, inline=True, fontsize=10)

        plt.xticks(())
        plt.yticks(())

        plt.show()


if __name__ == "__main__":
    mc =MatplotlibContour()
    mc.generate_figure()
