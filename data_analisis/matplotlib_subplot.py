#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_subplot.py
#   Last Modified : 2020-12-13 10:59
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt

# 父图形
plt.figure()

# 第1个子图形
plt.subplot(2, 1, 1)  # 分成2行1列,在第1行第1个位置画子图形,这样这个子图形就占用了上面一整行
# 在子图形中画一条直线
plt.plot([0, 1], [0, 1])  # x轴数据[0,1],y轴数据[0,1]

# 第2个子图形
plt.subplot(2, 3, 4)  # 分成2行3列,在第2行第1个位置画子图形(从第一行开始数)
# 在子图形中画一条直线
plt.plot([0, 1], [0, 2])  # x轴数据[0,1],y轴数据[0,2]

# 第3个子图形
plt.subplot(235)  # 分成2行3列,在第2行第2个位置画子图形;可以不使用逗号
# 在子图形中画一条直线
plt.plot([0, 1], [0, 3])  # x轴数据[0,1],y轴数据[0,3]

# 第4个子图形
plt.subplot(236)  # 分成2行2列,在第2行第3个位置画子图形;可以不使用逗号
# 在子图形中画一条直线
plt.plot([0, 1], [0, 4])  # x轴数据[0,1],y轴数据[0,4]

plt.show()
