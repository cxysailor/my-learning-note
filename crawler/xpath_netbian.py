#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_netbian.py
#   Last Modified : 2020-08-19 21:26
#   Describe      :
#
# ====================================================
import time
import os
import requests
from lxml import etree


class NetBiAnPic():
    """获取彼岸图网上的图片"""
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        self.url = 'http://pic.netbian.com/4kmeinv/'

    def get_infomation(self):
        """爬取信息"""
        # 爬取美女图的首页
        response = requests.get(url=self.url, headers=self.headers)
        # 可以手动设置编码格式 - 解决中文乱码问题，但是通常使用下面43行的做法
        #  response.encoding = 'gbk'
        page_text = response.text
        # 创建etree实例
        tree = etree.HTML(page_text)

        # 获取src与alt的属性值
        li_list = tree.xpath('//div[@class="slist"]//li')  # 获取所有相关的li标签
        return li_list

    def save_images(self):
        """爬取并保存图片"""
        # 创建图片存储目录
        if not os.path.exists('./images'):
            os.mkdir('./images')
        li_list = self.get_infomation()
        for li in li_list:
            img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]  # 图片的url
            ex_name = li.xpath('./a/img/@src')[0].split('.')[1]  # 图片的扩展名
            img_name = li.xpath('./a/img/@alt')[0] + '.' + ex_name  # 图片名称
            # 解决中文乱码问题 - 比较通用的办法，哪里有乱码就在哪里解决
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            #  print(img_url, img_name)

            # 爬取图片数据
            img_data = requests.get(url=img_url, headers=self.headers).content

            # 保存图片
            img_path = './images/' + img_name  # 图片路径
            with open(img_path, mode='wb') as fp:
                fp.write(img_data)
            print(img_name, 'Completed downloading!')
            time.sleep(0.5)


if __name__ == "__main__":
    nbap = NetBiAnPic()
    nbap.save_images()
    print('All Completed!')
