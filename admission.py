#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : admission.py
#   Last Modified : 2020-11-15 19:52
#   Describe      :
#
# ====================================================
import re
import pandas as pd


class GetDetailsAdmission():
    """处理云南招考院的录取日报数据"""
    def __init__(self, file_name='n.txt'):
        super(GetDetailsAdmission, self).__init__()
        self.file_name = file_name  # 需要读取的数据来源文件
        self.info_list = []  # 存储处理好的信息列表
        self.digit_list = []  # 临时存储分离出的数字(录取人数、最高分、最低分...)
        # 数据字典里需要动态改变值的键列表
        self.key_list = [
            'admission_num',
            'highest_score',
            'lowest_score',
            'first_solicit',
            'second_solicit',
            'third_solicit',
            'fouth_solicit'
        ]
        # DataFrame的列标题
        self.idx = [
            '录取批次',
            '科类代码',
            '科类名称',
            '院校代码',
            '院校名称',
            '录取人数',
            '最高分',
            '原始最低分',
            '第一次征集',
            '第二次征集',
            '第三次征集',
            '第四次征集'
        ]

    def reading_data(self):
        """读取数据文件"""
        with open(self.file_name, mode='r', encoding='utf-8') as fp:
            text = fp.read()
        return text

    def extract_data(self):
        """使用正则提取数据"""
        text = self.reading_data()
        pat = r'[\u4e00-\u9fa5]+\d[\u4e00-\u9fa5]{2}[0-9a-zA-Z]{4}[\u4e00-\u9fa5]+.*?\d+'
        result = re.findall(pat, text)
        return result

    def extract_figures(self, num):
        """拆分数字"""
        # 求余 - 取出最后3位数 150565535535535515526 --> 526以此类推
        s = num % 1000
        return s

    def data_handle(self):
        """处理提取出来的数据"""
        result = self.extract_data()
        for each in result:
            pat1 = r'[^\d+a-zA-Z]+|[0-9a-zA-Z]+'  # 选出非数字字母的字符|数字和字母
            r = re.findall(pat1, each)
            # 将提取出来的最后一串数字拆分成3位数一节
            num = int(r[5])
            flag = 0
            times = len(str(r[5])) // 3  # 计算需要循环的次数
            while flag < times + 1:
                s = self.extract_figures(num)
                # 将最后三位数舍弃 150565535535535515526 --> 150565535535535515 一直取完为止
                num = num // 1000
                if not s:  # 当s为0,循环终止
                    break
                self.digit_list.insert(0, s)  # 将拆分出来的数字放入列表的头部
                flag += 1
            # 把提取好的数据存储为一个字典
            info_dict = {
                'adm_batch': r[0],
                'family_code': r[1],
                'family_name': r[2],
                'institution_code': r[3],
                'institution_name': r[4],
                'admission_num': '',
                'highest_score': '',
                'lowest_score': '',
                'first_solicit': '',
                'second_solicit': '',
                'third_solicit': '',
                'fouth_solicit': ''
            }
            # 将提取出来的人数、最高分、最低分、征集志愿最低分依次写入字典
            # 但是有的学校有征集志愿，有的学校没有，故需要动态添加
            for i in range(len(self.digit_list)):
                info_dict[self.key_list[i]] = self.digit_list[i]
            # 清空临时存储数字的字典，以便处理下一个学校的数据
            self.digit_list = []
            # 将最终结果写入列表
            self.info_list.append(info_dict)
        return self.info_list

    def save_data(self):
        """使用Pandas将数据保存"""
        info_list = self.data_handle()
        df = pd.DataFrame(info_list)
        df.columns = self.idx
        df.to_csv('./nn.txt')
        # 按照文史类与理工类统计录取人数
        print(df.groupby('科类名称').sum())


if __name__ == "__main__":
    gda = GetDetailsAdmission()
    gda.save_data()
