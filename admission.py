#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : admission.py
#   Last Modified : 2020-08-26 16:59
#   Describe      : 
#
# ====================================================
import re
import pandas as pd

with open('./n.txt', mode='r', encoding='utf-8') as fp:
    text = fp.read()
pat = '[\u4e00-\u9fa5]+\d[\u4e00-\u9fa5]{2}[0-9a-zA-Z]{4}[\u4e00-\u9fa5]+.*?\d+'
result = re.findall(pat, text)
info_list = []
digit_list = []
count = 0
for each in result:
    pat1 = '[^\d+a-zA-Z]+|[0-9a-zA-Z]+'  # 选出非数字字母的字符|数字和字母
    r = re.findall(pat1, each)
    num = int(r[5])
    flag = 0
    times = len(str(r[5])) // 3
    while flag < times + 1:
        s = num % 1000
        num = num // 1000
        #  print(txt)
        if not s:
            break
        digit_list.append(s)
        flag += 1
    info_dict = {
        'adm_batch': r[0],
        'family_code': r[1],
        'family_name': r[2],
        'institution_code': r[3],
        'institution_name': r[4],
        'admission_num': digit_list[-1],
        'highest_score': digit_list[-2]
    }
    count += 1
    digit_list = []
    info_list.append(info_dict)
#  print(digit_dicts)
idx = ['录取批次',
       '科类代码',
       '科类名称',
       '院校代码',
       '院校名称',
       '录取人数',
       '最高分'
    ]
df = pd.DataFrame(info_list)
df.columns = idx
df.to_csv('./nn.txt')
#  print(df['admission_num'].sum())
print(df.groupby('科类名称').sum())
