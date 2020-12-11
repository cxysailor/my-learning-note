#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_image.py
#   Last Modified : 2020-12-11 09:31
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np


class MatplotlibImage(object):
    """docstring for MatplotlibImage"""
    def __init__(self):
        super(MatplotlibImage, self).__init__()
        # 图片数据
        self.a = np.array([
            0.313660827978, 0.36534818405, 0.423733120134,
            0.36534818405, 0.439599930621, 0.525083754405,
            0.423733120134, 0.525083754405, 0.651536351379
        ]).reshape(3, 3)

    def generate_figure(self):
        # 根据数据画图
        plt.imshow(self.a, interpolation='nearest', cmap='bone', origin='lower')
        # 添加颜色条
        plt.colorbar()

        plt.xticks(())
        plt.yticks(())

        plt.show()


if __name__ == "__main__":
    mi = MatplotlibImage()
    mi.generate_figure()
