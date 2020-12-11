#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_annotation.py
#   Last Modified : 2020-12-09 10:44
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class AddAnnotation(object):
    """docstring for AddAnnotation"""
    def __init__(self):
        super(AddAnnotation, self).__init__()
        self.x = np.linspace(-3, 3, 50)
        self.y = self.x * 2 + 1
        self.title = 'Figure of function: y = 2x + 1'

    def generate_figure(self):
        plt.figure(num=1, figsize=(8, 5))
        plt.plot(self.x, self.y)

        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))

        # 画出点(1, 3)即x=1,y=2×1+1=3
        x0 = 1
        y0 = 2 * x0 + 1
        plt.scatter(x0, y0, color='green', s=50)
        # 从该点画一条垂线与x轴相交
        plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)  # k--表示黑色短划线

        # 添加标注 - 方法1 -画一个箭头指向该点，并标注说明文字2x+1=3
        plt.annotate(r'$2x + 1 = %s$' % y0, 
                xy=(x0, y0), xycoords='data',
                xytext=(+30, -30), textcoords='offset points',
                fontsize=16,
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2', color='red'))
        # 添加标注 - 方法2 - 添加一段文字描述
        plt.text(-3.7, 7, r'$The\ quick\ brown\ fox\ jumps\ over\ a\ lazy\ dog.\ \mu\ \sigma_i\ \alpha^t$',
                fontdict={'size': 16, 'color': 'red'})

        plt.title(self.title, loc='right')

        plt.show()


if __name__ == "__main__":
    aa = AddAnnotation()
    aa.generate_figure()
