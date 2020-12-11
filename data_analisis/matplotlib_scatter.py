#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_scatter.py
#   Last Modified : 2020-12-09 17:25
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class MatplotlibScatter(object):
    """散点图"""
    def __init__(self):
        super(MatplotlibScatter, self).__init__()
        self.n = 1024
        self.X = np.random.normal(0, 1, self.n)
        self.Y = np.random.normal(0, 1, self.n)
        # 设置颜色
        self.T = np.arctan2(self.Y, self.X)

    def generate_figure(self):
        plt.scatter(self.X, self.Y, s=75, c=self.T, alpha=0.5)
        plt.xlim(-1.5, 1.5)
        plt.ylim(-1.5, 1.5)
        # 隐藏x、y轴的刻度
        plt.xticks(())
        plt.yticks(())
        print(self.T)

        plt.show()


if __name__ == "__main__":
    ms = MatplotlibScatter()
    ms.generate_figure()
