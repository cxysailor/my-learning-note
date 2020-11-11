#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : bs_sanguoyanyi.py
#   Last Modified : 2020-11-08 10:15
#   Describe      :
#
# ====================================================
import time
import requests
from bs4 import BeautifulSoup as bs


if __name__ == "__main__":
    # UA伪装
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    # 对首页进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # 获取首页数据
    page_text = requests.get(url=url, headers=headers).text
    #  print(page_text)
    # 在首页数据中解析出章节标题及其对应的内容链接
    soup = bs(page_text, 'lxml')  # 实例化一个bs4对象，并将获取的首页数据加载
    # 解析标题和url
    li_list = soup.select('.book-mulu > ul > li')  # 定位到li标签
    with open('./sanguoyanyi.txt', mode='w', encoding='utf-8') as fp:
        # 遍历出li标签的所有a标签并获取信息
        for li in li_list:
            title = li.a.string  # 标题
            detail_url = 'https://www.shicimingju.com' + li.a['href']  # 对应内容的url
            # 对detail_url发起请求，解析出章节内容
            detail_page_text = requests.get(url=detail_url, headers=headers).text
            # 解析章节内容
            detail_soup = bs(detail_page_text, 'lxml')
            # 定位到class为chapter-conent的div标签
            div_tag = detail_soup.find('div', class_='chapter_content')
            # 获取内容
            content = div_tag.text
            # 保存
            fp.write(title + content + '\n')
            print(title, '爬取成功!')
            time.sleep(2)
