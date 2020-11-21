#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_example.py
#   Last Modified : 2020-11-21 22:40
#   Describe      : 
#
# ====================================================
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

font = {
    'family': 'WenQuanYi Micro Hei',
    'weight': 'bold',
    'size': 10
}
matplotlib.rc('font', **font)

#  x = range(2, 26, 2)
#  y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
x = range(0, 120)
y = [random.randint(20,35) for i in range(120)]
plt.figure(figsize=(20, 9))
_xtick_labels = [f"10点{i}分" for i in range(60)]
_xtick_labels += [f"11点{i}分" for i in range(60)]
plt.plot(x, y)
plt.xticks(x[::3], _xtick_labels[::3], rotation=45)
plt.xlabel('时间')
plt.ylabel("温度")
plt.title('10点到12点的每分钟温度情况')
#  plt.savefig('./t1.png')
plt.show()
