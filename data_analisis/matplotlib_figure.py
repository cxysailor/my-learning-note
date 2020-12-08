#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_figure.py
#   Last Modified : 2020-12-07 20:53
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class MatplotlibFigure(object):
    """Matplotlib到figure方法"""
    def __init__(self):
        super(MatplotlibFigure, self).__init__()
        # x轴的数据
        self.x = np.linspace(-1, 1, 50)
        # y轴的数据
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2

    def generate_figure(self):
        """生成图形"""
        # 第一个图形 - 以y1为y轴数据
        plt.figure()
        plt.plot(self.x, self.y1)
        # 第二个图形 - 以y2为y轴数据
        plt.figure(num=5)
        plt.plot(self.x, self.y1)
        # 设置一些属性 - 颜色、线条宽度、线条样式
        plt.plot(self.x, self.y2, color='red', linewidth=5, linestyle='dashdot')
        plt.show()


if __name__ == "__main__":
    mf = MatplotlibFigure()
    mf.generate_figure()
