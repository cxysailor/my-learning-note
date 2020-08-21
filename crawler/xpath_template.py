#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_template.py
#   Last Modified : 2020-08-21 15:06
#   Describe      : 爬取站长素材中的免费模板
#
# ====================================================
import os
import time
import requests
from lxml import etree


class TemplateGet():
    """docstring for TemplateGet"""
    def __init__(self):
        super(TemplateGet, self).__init__()
        self.url = 'http://sc.chinaz.com/jianli/free.html'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        self.url_list = []
        self.temp_name = []

    def get_page(self, url):
        """获取免费模板页的网页源代码"""
        page_text = requests.get(url=url, headers=self.headers).text
        tree = etree.HTML(page_text)
        return tree

    def get_max_page_num(self):
        """获取页面的最大数值"""
        t = self.get_page(self.url)
        # 获取页面的最大数值 - 即共有多少个页面
        max_b = t.xpath('//div[@class="pagination fr clearfix clear"]/a/b')[-1]
        max_page = int(max_b.xpath('./text()')[0])
        return max_page

    def get_each_url(self, url):
        """获取每一页的url以及模板的名称"""
        tree = self.get_page(url)
        # 获取每个模板对应的a标签
        each_a_list = tree.xpath('//*[@id="container"]/div/a')
        for each_a in each_a_list:
            # 获取每个模板对应的url
            each_url = each_a.xpath('./@href')[0]
            # 获取每个模板的名称
            each_name = each_a.xpath('./img/@alt')[0].encode('iso-8859-1').decode('utf-8')
            self.url_list.append(each_url)
            self.temp_name.append(each_name)
        return self.url_list, self.temp_name

    def download_save_data(self, url):
        """下载一个页面中每个免费模板并保存"""
        if not os.path.exists('./template_lib'):
            os.mkdir('./template_lib')
        urls, names = self.get_each_url(url)
        for n in range(len(urls)):
            # 爬取每个模板的详情页面内容
            each_page_text = requests.get(url=urls[n], headers=self.headers).text
            each_tree = etree.HTML(each_page_text)
            # 获取模板的下载链接
            down_url = each_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a[1]/@href')[0]
            #  print(down_url)
            # 下载模板
            each_data = requests.get(url=down_url, headers=self.headers).content
            # 保存文件路径
            file_path = './template_lib/' + str(n + 1) + names[n] + '.rar'
            # 保存下载的模板
            with open(file_path, mode='wb') as fp:
                fp.write(each_data)
            print(f'第{n}个下载完成')
            time.sleep(2)


if __name__ == "__main__":
    tg = TemplateGet()
    max_p = tg.get_max_page_num()  # 免费模板的页面总数
    #  print(max_page)
    # 这个循环控制的是每一个页面
    for nu in range(2):
    #  for nu in range(max_p):  # 下载所有的免费模板页面
        url = 'http://sc.chinaz.com/jianli/free'  # 由于第一页与其他页面的url不一样，需要特殊处理
        if nu == 0:
            url = url + '.html'
        else:
            url = url + '_' + str(nu + 1) + '.html'  # 第二页是free_2.html结尾
        print(url)
        tg.download_save_data(url)
    print('Done !')
