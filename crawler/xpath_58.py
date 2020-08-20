#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_demo.py
#   Last Modified : 2020-08-18 20:27
#   Describe      :
#
# ====================================================
import time
import random
import requests
from lxml import etree


class Crawl58SecondHandHouse():
    """爬取58同城上的二手房信息"""
    def __init__(self):
        self.url = 'https://sh.58.com/pudongxinqu/ershoufang/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.proxy = [
            {'http': 'http://102.69.32.1:8080'},
            {'http': 'http://112.111.77.191:9999'},
            {'http': 'http://123.55.102.240:9999'},
            {'http': 'http://94.51.83.2:8080'},
            {'http': 'http://178.210.129.150:1234'},
            {'http': 'http://185.222.59.161:5836'},
            {'http': 'http://183.89.41.17:8080'},
            {'http': 'http://175.42.123.143:9999'},
            {'http': 'http://168.228.193.217:999'},
            {'http': 'http://51.158.29.37:5836'}
        ]
        self.num = 1
        self.li_lists = []

    def get_info(self):
        """获取数据"""
        # 爬取网页
        page_text = requests.get(url=self.url, headers=self.headers, proxies=random.choice(self.proxy)).text
        # 实例化对象
        tree = etree.HTML(page_text)
        # 获取页面总数
        pages = tree.xpath('//div[@class="pager"]/a')
        max_page = pages[-2].xpath('./span/text()')[0]
        max_page = int(max_page)
        # 爬取每一页的信息
        for n in range(0, max_page):
            # 新的url - 每一页的url
            each_url = self.url + 'pn' + str(n + 1)
            print(each_url)
            # 爬取新的url
            each_page_text = requests.get(url=each_url, headers=self.headers, proxies=random.choice(self.proxy)).text
            #  print(each_page_text)
            each_page_tree = etree.HTML(each_page_text)
            # 获取class属性为house-list-wrap的ul标签下的所有的li标签
            li_list = each_page_tree.xpath('//ul[@class="house-list-wrap"]/li')
            self.li_lists.append(li_list)
            time.sleep(0.5)
        return self.li_lists

    def saving_info(self):
        """保存数据"""
        lis = self.get_info()
        with open('./ershoufang.txt', mode='w', encoding='utf-8') as fp:
            for lls in lis:
                for li in lls:
                    try:
                        # 房源标题
                        title = li.xpath('./div[2]/h2/a/text()')[0]
                        # 总价
                        price = str(li.xpath('./div[3]/p[1]/b/text()')[0]) \
                                + li.xpath('./div[3]/p[1]/text()')[0]
                        # 单价
                        unit_price = li.xpath('./div[3]/p[2]/text()')[0]
                        # 房型布局
                        layout = li.xpath('./div[2]/p[1]/span[1]/text()')[0]
                        # 房子面积
                        area = li.xpath('./div[2]/p[1]/span[2]/text()')[0]
                        # 房子朝向
                        toward = li.xpath('./div[2]/p[1]/span[3]/text()')[0]
                        # 楼层
                        layer = li.xpath('./div[2]/p[1]/span[4]/text()')[0]
                        # 楼盘名称
                        name = li.xpath('./div[2]/p[2]/span[1]/a[1]/text()')[0]
                        # 楼盘坐落地区
                        strict = li.xpath('./div[2]/p[2]/span[1]/a[2]/text()')[0]
                        # 楼盘地址
                        location = li.xpath('./div[2]/p[2]/span[1]/a[3]/text()')[0] \
                                + li.xpath('./div[2]/p[2]/span[2]/text()')[0]
                    except IndexError as e:
                        #  print(e)
                        location = li.xpath('./div[2]/p[2]/span[1]/a[3]/text()')[0]
                    #  保存数据
                    fp.write(((str(self.num) + '.'
                               + title + ','
                               + price + ','
                               + unit_price + ','
                               + layout + ','
                               + str(area) + ','
                               + toward + ','
                               + layer + ','
                               + name + ','
                               + strict + ','
                               + location
                               + '\n')))
                    self.num += 1


if __name__ == "__main__":
    c = Crawl58SecondHandHouse()
    c.saving_info()
    print('All Done !')
