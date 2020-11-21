#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : multiple_table.py
#   Last Modified : 2020-11-08 10:10
#   Describe      : 
#
# ====================================================

for num1 in range(1, 10):
    for num2 in range(1, num1 + 1):
        print('%d x %d = %2d' % (num2, num1, num1 * num2), end=' ')
    print('')
