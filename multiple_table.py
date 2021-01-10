#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : multiple_table.py
#   Last Modified : 2021-01-09 11:14
#   Describe      : 
#
# ====================================================


class MultiplicationTable(object):
    """九九乘法表"""

    def multiplication_table(self):
        for num1 in range(1, 10):
            for num2 in range(1, num1 + 1):
                print('%d x %d = %2d' % (num2, num1, num1 * num2), end=' ')
            print('')


if __name__ == "__main__":
    mt = MultiplicationTable()
    mt.multiplication_table()
