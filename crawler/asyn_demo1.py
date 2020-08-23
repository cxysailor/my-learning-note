#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : asyn_demo1.py
#   Last Modified : 2020-08-22 18:59
#   Describe      :
#
# ====================================================
import time
from multiprocessing.dummy import Pool

name_list = [
        'Jacky',
        'Tom Hanks',
        'Angelina Julie'
        ]


def get_page(string):
    print('正在下载..', string)
    time.sleep(2)
    print('下载成功:', string)


if __name__ == "__main__":
    start_time = time.time()
    #  for i in range(len(name_list)):
    #      get_page(name_list[i])
    # 创建一个包含3个进程的进程池
    pool = Pool(3)
    # 将列表中的每一个元素传给get_page()执行
    pool.map(get_page, name_list)
    end_time = time.time()
    print(f'用时:{start_time - end_time}秒!')
