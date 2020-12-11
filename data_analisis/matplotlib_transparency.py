#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_transparency.py
#   Last Modified : 2020-12-09 14:11
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class Transparency(object):
    """docstring for AddAnnotation"""
    def __init__(self):
        self.x = np.linspace(-3, 3, 50)
        self.y = self.x * 0.1

    def generate_figure(self):
        plt.figure(num=1, figsize=(8, 5))
        # 设置zorder=1
        plt.plot(self.x, self.y, linewidth=10, zorder=1)
        plt.ylim(-2, 2)

        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))

        # 对标签的字体和边框进行设置
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontsize(12)
            # bbox - bounding box
            label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

        plt.show()


if __name__ == "__main__":
    t = Transparency()
    t.generate_figure()
