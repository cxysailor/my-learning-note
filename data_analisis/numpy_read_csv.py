#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : numpy_read_csv.py
#   Last Modified : 2020-12-05 13:16
#   Describe      : 
#
# ====================================================

import numpy as np


def generate_numbers(file_path):
    """生成随机数字并保存为csv文件"""
    with open(file_path, mode='w', encoding='utf-8') as f:
        for _ in range(500):
            for i in range(4):
                data = np.random.randint(0, 5000000)
                if i < 3:
                    f.write(str(data) + ',')
                else:
                    f.write(str(data))
            f.write('\n')


#  generate_numbers('./data_gb.csv')
#  generate_numbers('./data_us.csv')

us_file_path = './data_us.csv'
data_us = np.loadtxt(us_file_path, delimiter=',', dtype='int')
data_us1 = np.loadtxt(us_file_path, delimiter=',', dtype='int', unpack=True)
print(data_us)
print('*' * 50)
print(data_us1)
