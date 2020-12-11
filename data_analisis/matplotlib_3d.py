#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_3d.py
#   Last Modified : 2020-12-11 22:27
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class Mpl3D(object):
    """docstring for Mpl3D"""
    def __init__(self):
        super(Mpl3D, self).__init__()
        self.x = np.arange(-4, 4, 0.25)
        self.y = np.arange(-4, 4, 0.25)

    def generate_figure(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        X, Y = np.meshgrid(self.x, self.y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)

        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
        ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
        ax.set_zlim3d(-2, 2)

        plt.show()


if __name__ == "__main__":
    md = Mpl3D()
    md.generate_figure()
