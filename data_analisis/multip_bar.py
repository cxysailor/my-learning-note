#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : multip_bar.py
#   Last Modified : 2020-11-30 10:25
#   Describe      : 
#
# ====================================================


from matplotlib import pyplot as plt
#  from matplotlib import font_manager


class MultiBarDemo(object):
    """绘制多次条形图"""
    def __init__(self):
        super(MultiBarDemo, self).__init__()
        # 解决中文显示的问题
        plt.rcParams['font.family'] = ['WenQuanYi Micro Hei']
        plt.rcParams['axes.unicode_minus'] = False
        #  self.my_font = font_manager.FontProperties(fname='/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc')
        # 数据
        self.x = ['星球崛起3:终极之战', '敦克尔克', '蜘蛛侠:英雄归来', '战狼2']  # 电影名称
        # 14、15、16三天的票房数据
        self.y_16 = [15746, 312, 4497, 319]
        self.y_15 = [12357, 156, 2045, 168]
        self.y_14 = [2358, 399, 2358, 362]
        # 条形图的宽度
        self.BAR_WIDTH = 0.2 
        # 设置图形的大小
        plt.figure(figsize=(20, 8), dpi=80)

    def show_demo(self):
        """画图形并显示"""
        # 条形图的间隔距离
        x_14 = list(range(len(self.x)))  # [0, 1, 2, 3]
        x_15 = [i + self.BAR_WIDTH for i in x_14]  # [0.2, 1.2, 2.2, 3.2]
        x_16 = [i + self.BAR_WIDTH * 2 for i in x_14]  # [0.4, 1.4, 2.4, 3.4]
        # 分别画出三天的票房条形图
        plt.bar(x_14, self.y_14, width=self.BAR_WIDTH, label='14日')
        plt.bar(x_15, self.y_15, width=self.BAR_WIDTH, label='15日')
        plt.bar(x_16, self.y_16, width=self.BAR_WIDTH, label='16日')
        # 显示图例
        plt.legend()
        # 设置x轴的刻度
        plt.xticks(x_15, self.x)
        # 显示图形
        plt.show()


if __name__ == "__main__":
    mbd = MultiBarDemo()
    mbd.show_demo()
