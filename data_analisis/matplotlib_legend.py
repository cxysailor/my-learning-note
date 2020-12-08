#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_legend.py
#   Last Modified : 2020-12-08 22:17
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class LengendSetting(object):
    """docstring for LengendSetting"""
    def __init__(self):
        super(LengendSetting, self).__init__()
        self.x = np.linspace(-3, 3, 50)
        self.y1 = self.x * 2 + 1
        self.y2 = self.x ** 2
        self.new_ticks = np.linspace(-1, 2, 5)

    def generate_figure(self):
        plt.figure()
        plt.xlim((-1, 2))
        plt.ylim((-2, 3))
        plt.xlabel('I am x')
        plt.ylabel('I am y')
        plt.xticks(self.new_ticks)
        plt.yticks([-2, -1.8, -1, 1.22, 3],
                [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
        # 要加上一个逗号
        l1, = plt.plot(self.x, self.y2, color='red', linestyle='--', label='Up')
        l2, = plt.plot(self.x, self.y1, label='Down')

        # 使用labels参数就不再使用上面设置的label了
        plt.legend(handles=[l1, l2], labels=['Conic', 'Straight line'], loc='best')

        plt.show()


if __name__ == "__main__":
    ls = LengendSetting()
    ls.generate_figure()
