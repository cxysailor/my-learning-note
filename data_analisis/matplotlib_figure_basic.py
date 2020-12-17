#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : matplotlib_figure_basic.py
#   Last Modified : 2020-12-15 22:26
#   Describe      : 
#
# ====================================================

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 2, 100)
# there are essentially two ways to use Matplotlib:
# Explicitly create figures and axes, and call methods on them (the "object-oriented (OO) style")
# Rely on pyplot to automatically create and manage the figures and axes, and use pyplot functions for plotting

# So one can do (OO-style)
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x ** 2, label='quadratic')
ax.plot(x, x ** 3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('Simple Plot')
ax.legend()

# or (pyplot-style)
plt.figure(num=2)
plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
plt.legend()

plt.show()
